; ***********************************************************
;
; file: FinalAutoturn.asm
; target: PIC16f684 on PICKit 1
; Jan 2016
; author: MartinF
; For G.Balcita
;
;
; This program codes for a line following robot.
;
; ***********************************************************

	; use PIC 16F684
	list		p=16f684
	#include	<p16f684.inc>

	; set configuration word.
	__CONFIG	_FCMEN_OFF & _IESO_OFF & _BOD_OFF & _CPD_OFF & _CP_OFF & _MCLRE_OFF & _PWRTE_OFF & _WDT_OFF & _INTRC_OSC_NOCLKOUT

	; -------------------------------------------------------
	; global variable declarations.
	; -------------------------------------------------------
;Wait and Persist are set to delay different amounts of time
Turn equ 0x29
count3 equ 0x25
count2 equ 0x23
count equ 0x28
Left  equ 0x24
Right equ	0x22
StopR  equ 0x26
StopL  equ 0x27	


	; -------------------------------------------------------
	; reset vector.  this is where the PCL is set after
	; power on and reset.
	; -------------------------------------------------------

	org	0x00
	goto	main

Endofline 
	movlw 0x04
	movwf PORTA 
	movlw 0x20
	movwf PORTC
	
	movlw 0x08
	movwf count3
	call Persist
	
	clrf PORTA 
	clrf PORTC
	
	movlw 0x04
	movwf PORTA  
	movlw 0x12
	movwf PORTC

	movlw 0x13
	movwf count3
	call Persist ; Delay 

	call sample_adc
	btfss Left,1 
	goto $-2
	return

	
Persist
	nop			; consume one cycle

	decfsz	count,f	; decrement first counter
	goto	Persist		;  until reaching zero

	movlw	0xff		; reload first counter
	movwf	count

	decfsz	count2,f	; decrement second counter
	goto	Persist		;  until reaching zero

	movlw	0x35		; reload second counter
	movwf	count2

	decfsz	count3,f	; decrement third counter
	goto	Persist		;  until reaching zero

	movlw	0x15		; reload third counter
	movwf	count3


	return
wait
	
	movlw 0xff
	movwf count  
	decfsz count,f	
	goto $-1
	movwf count  
	decfsz count,f	
	goto $-1
	clrw
	return
ReverseL
	
	movlw 0x04
	movwf PORTA
	movlw 0x00
	
	movlw 0x01 ;Cancel momenteum
	movwf count3 
	call Persist
	return
ReverseR
	movlw 0x20
	movwf PORTC
	movlw 0x00

	movlw 0x01 ;Cancel momenteum
	movwf count3 
	call Persist
	return
	

MotorL
	clrf PORTA
	movlw B'00010000' 
	 
	btfsc Right,1 
    call ReverseL
	movwf PORTA
	clrf Right	
 	return
MotorR
	movlw B'00010000'
    clrf PORTC
	btfsc Left,1 
	call ReverseR
	movwf PORTC
	clrf Left
	return

sample_adc
	bcf	STATUS,RP0	; enter bank 0
	movlw	B'10011101'	; Right justified, Vdd ref, AN0, GO off, ADC on
	movwf	ADCON0
	bsf		ADCON0,GO	; start ADC
	btfsc ADCON0,GO ; This little loop acts a method to ensure the ADC reads properly, when the ADC is done its operation it will set go to clear automatically
	goto $-1 
	

	movf	ADRESH,W		;
	movwf	Right
;	call	wait
	
	bcf	STATUS,RP0	; enter bank 0
	movlw	B'10011001'	; Right justified, Vdd ref, AN0, GO off, ADC on
	movwf	ADCON0
	bsf		ADCON0,GO	; start ADC
	btfsc ADCON0,GO ;
	goto $-1 

	movf	ADRESH,W		;
	movwf	Left
	andwf   Right,0 ; And the Two inputs and send to Turn
	movwf   Turn 
	clrw 
	return


main
	; -------------------------------------------------------
	; program's main entry point.
	; -------------------------------------------------------

	; init PortA

	movlw	B'11000000'	; RA2 RA4 RA5
; banksel TRISA
	bsf	STATUS,RP0	; enter bank 1
	movwf	TRISA		; configure I/O

	movlw   B'10001101'; cONFIGURE RC2 and RC3 (AN6 and AN7)
	;banksel TRISC 
	movwf   TRISC 
	
	movlw	B'11000000'	; Set AN6 AN7 
	;banksel ANSEL 
	movwf	ANSEL
	
	movlw	B'00110000'	; set clock to internal
	;banksel ADCON1
	movwf	ADCON1
			
	
	bcf	STATUS,RP0	; enter bank 0
	movlw 0xff
	movwf count
	movlw 0x35 
	movwf count2
	movlw 0x0f
	movwf count3
	
	movlw B'00010000' ;get pastline
	movwf PORTC 
	
	movlw B'0010000'
	movwf PORTA 

	call Persist

		;ADCON0 = b'00000001'; 
		;x_______ 0 = left justified / 1 = right justified              
		;_x______ 0 = voltage reference from vdd / 1 voltage reference from aref pin 
		;__x_____ not configured (always set to 0) 
		;___xxx__ Adress of pins to read (000 = an0 / 001 = an1) 
		;______x_ GO/Done Bit 
		;_______x adc enable bit 1 = on / 0 = off (consumes no power in off state) 

loop
	; -------------------------------------------------------
	; program's main loop.
	; -------------------------------------------------------
	bcf	STATUS,RP0	; enter bank 0
	clrw
	clrf Turn
	call sample_adc
	
	call MotorR
	clrw
	call MotorL
  
    btfsc Turn,1 
	call Endofline
	clrf Turn
	goto	loop		; repeat forever

	end
