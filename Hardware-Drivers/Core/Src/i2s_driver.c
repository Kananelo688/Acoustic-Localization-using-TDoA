/*
 * This is source file for configuring all registers and port pin for i2s interface on STM32F051C6
 *
 *  Created on: Aug 25, 2023
 *      Author: chabeli Kananelo
 */

/*Includes*/
#include "stm32f0xx.h" 				//TO USED FOR STM32F0 Peripherals and Configuration

/*Preprocessor Directives*/
#define  TRUE     1
#define  FALSE    0


/**
 * @brief : The function configures GPIO pins PA4, PA5 and PA7 for use by I2S interface.
 * 			PA0 pin is also configures for interrupt.
 * 			Additionally, GPIOB pins PB0-7 are also configure in output mode to be used for testing purpose
 *
 * @param: None
 * @retval: None
 * */
void configure_GPIO(void)
{
	GPIOA->MODER|=GPIO_MODER_MODER3_1|
			GPIO_MODER_MODER4_1|
			GPIO_MODER_MODER7_1;			// SET PA4, PA5 AND PA7 TO ALTERNATIVE FUNCTION MODE


}

/**
 * @brief : This function enable clock signals for GPIOA, GPIOB and I2S Peripherals
 *
 * @param: None
 * @retval: None
 *
 * */
void clock_enable(void){
	RCC->AHBENR|=RCC_AHBENR_GPIOAEN|RCC_AHBENR_GPIOBEN;		//ENABLE CLOCK SIGNAL FOR GPIOA and GPIOB
	RCC->APB2ENR|=RCC_APB2ENR_SPI1EN;						//ENABLE CLOCK SIGNAL FOR SPI
}
/**
 * @brief: This function configure and set all registers of
 *
 *
 * @param: None
 * @retval: None
 * */
void configure_I2S(void){

}
/**
 * @brief: This function enable interrupts for GPIOA as well as I2S interrupts
 *
 *
 * @param: None
 * @retval: None
 * */
void interrupts_enable(void)
{

}
/**
 * @brief: This function takes an 8-bit integer and write it to the output data register of GPIOB.
 * It will be used for testing in debugging purposes.
 *
 * @param: val - an 8-bit integer for writing into ODR of GPIOB
 * @retval: None
 *
 * */
void write_GPIOB(uint8_t value)
{
	GPIOB-> ODR|=value;
}
/**
 * @brief: This function takes a pointer to the data buffer and the length of that buffer, and writes I2S data into it.
 * The function is used in Poll-mode.
 *
 * @param: data- a pointer o the data buffer(Array) for storing data read from I2S bus interface
 * @retval: None
 * */
void read_data(uint16_t *data, uint32_t len)
{

}
/**
 * @brief: Interrupt Service Routine for I2S interrupts
 *
 * @param: None
 * @retval: None
 * */
// TO DO
/**
 * @brief: Interrupt Service Routine for GPIOA interrupts
 *
 * @param: None
 * @retval:None
 * */
//TO DO







