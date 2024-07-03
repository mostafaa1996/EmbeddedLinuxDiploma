//******************************************************************************/
/**
 * \file Icu_core.c
 * \brief Input Capture Unit (ICU) module source file
 * \details
 * This file contains implementation for the Input Capture Unit (ICU) module.
 *
 * \copyright Copyright 2021 . Mostafa Hamdy
 *
 * \ingroup hal
 *
 * \{
 *
 * **Changelog**
 * | Version |       Author      |               Date |                       Note                       |
 * |:-------:|:-----------------:|:---------------------------------:|:------------------------------------------------:|
 * |   1.0   |  Mostafa Hamdy    |  07.01.2024.20:27:00 (UTC+01:00)  | Fixing code according to coding guidelines |
 */
/******************************************************************************/

/******************************************************************************
* Includes
*******************************************************************************/
#include "Icu_core.h"

/******************************************************************************
* Module Preprocessor Constants
*******************************************************************************/

/******************************************************************************
* Module Preprocessor Macros
*******************************************************************************/

/******************************************************************************
* Module Typedefs
*******************************************************************************/
/** \brief Array of structures to configure the ICU Modules */
extern ICU_strIcuConfigs_t str_icuCfg[];

/******************************************************************************
* Module Variable Definitions
*******************************************************************************/

/******************************************************************************
* Function Prototypes
*******************************************************************************/


/******************************************************************************
* Function Definitions
*******************************************************************************/

/**
 * \brief Initialize the CCP Module as Input Capture Mode 
 * \details
 * 
 * \pre
 * 
 * \post
 * 
 * \param[in] ICU_Modules_t en_ICUModule
 * \return void
 * 
 * \b Example:
 * \code
 *  ICU_Init();
 * \endcode
 * 
 * \see Device datasheet
 * 
 * <br><b> - HISTORY OF CHANGES - </b>
 *  
 * <table align="left" style="width:800px">
 * <tr><td> Date       </td><td> Software Version </td><td> Initials </td>
 * <td> Description </td></tr>
 * <tr><td> 11.04.2021. 02:07:02 (UTC+01:00) </td><td> 1.0.0 </td><td> YOUR_INITIALS </td>
 * <td> Interface Created </td></tr>
 * </table><br><br>
 * <hr>
 * 
 */
void ICU_Init(ICU_Modules_t en_ICUModule)
{
    /* Configure CCPx on Input Capture Mode */
    ICU_ModeEnable (en_ICUModule);
    /* Configure the input capture unit mode */
    ICU_moduleCfg (en_ICUModule);
}

/**
 * \brief Set interrupt handler for ICU Module
 * \details
 * This function sets interrupt handler for specified ICU Module.
 * \pre
 * 1. Pointer must be different from NULL.
 * 2. ICU Module must be inside allowed Module number range.
 * \post
 * 1. Function sets interrupt handler function for specified ICU Module.
 * 
 * \param [in] Module ICU Module
 * \param [in] interruptHandler Pointer to callback function
 * \return status Returns 0 if pointer to callback function is different from 
 *                NULL, otherwise returns 1
 * 
 * \b Example:
 * \code
 * uint32_t mathAdd(uint16_t f1, uint16_t f2);
 * 
 * uint32_t mathAdd(uint16_t f1, uint16_t f2)
 * {
 *      return (uint32_t)(f1 + f2);
 * }
 * 
 *  uint8_t status = ICU_InterruptHandlerSet(ICU_MODULE_1, &mathAdd);
 * \endcode
 * 
 * \see Device datasheet
 * 
 * <br><b> - HISTORY OF CHANGES - </b>
 *  
 * <table align="left" style="width:800px">
 * <tr><td> Date       </td><td> Software Version </td><td> Initials </td>
 * <td> Description </td></tr>
 * <tr><td> 28.02.2021. 15:09:10 (UTC+01:00) </td><td> 1.0.0 </td><td> MK </td>
 * <td> Interface Created </td></tr>
 * </table><br><br>
 * <hr>
 * 
 */
uint8_t ICU_InterruptHandlerSet(ICU_enIcuInterruptMode_t en_icuModuleInterrupt, void * interruptHandler)
{
    uint8_t status;
    
    if(interruptHandler != NULL)
    {
        status = 0u;
    }
    else
    {
        status = 1u;
    }
    
    return status;
}

/**
 * \brief Set interrupt handler for ICU Timer Module
 * \details
 * This function sets interrupt handler for specified ICU Timer Module.
 * \pre
 * 1. Pointer must be different from NULL.
 * 2. ICU Timer Module must be inside allowed Module number range.
 * \post
 * 1. Function sets interrupt handler function for specified ICU Module.
 * 
 * \param [in] Module ICU Timer Module
 * \param [in] interruptHandler Pointer to callback function
 * \return status Returns 0 if pointer to callback function is different from 
 *                NULL, otherwise returns 1
 * 
 * \b Example:
 * \code
 * uint32_t mathAdd(uint16_t f1, uint16_t f2);
 * 
 * uint32_t mathAdd(uint16_t f1, uint16_t f2)
 * {
 *      return (uint32_t)(f1 + f2);
 * }
 * 
 *  uint8_t status = ICU_OverflowInterruptHandlerSet(ICU_MODULE_1, &mathAdd);
 * \endcode
 * 
 * \see Device datasheet
 * 
 * <br><b> - HISTORY OF CHANGES - </b>
 *  
 * <table align="left" style="width:800px">
 * <tr><td> Date       </td><td> Software Version </td><td> Initials </td>
 * <td> Description </td></tr>
 * <tr><td> 28.02.2021. 15:09:10 (UTC+01:00) </td><td> 1.0.0 </td><td> MK </td>
 * <td> Interface Created </td></tr>
 * </table><br><br>
 * <hr>
 * 
 */
uint8_t ICU_OverflowInterruptHandlerSet(ICU_Modules_t en_ICUModule, void * interruptHandler)
{
    uint8_t status;
    
    if(interruptHandler != NULL)
    {
        status = 0u;
    }
    else
    {
        status = 1u;
    }
    
    return status;
}

/**
 * \brief  
 * \brief Requirement ID:PXM004-103507
 * \details
 * 
 * \pre
 * CCPx configured as Input capture Mode
 * \post
 * 
 * \param[in] ICU_Modules_t en_ICUModule
 * \return 
 * 
 * \b Example:
 * \code
 *  ICU_ModuleCfg (CCP_MODULE_1,
 *                 en_IcuMode = ICU_EDGE_DETECT
 *                 en_IcuClkSrc = ICU_SYSTEM_CLK)
 * \endcode
 * 
 * \see Device datasheet
 * 
 * <br><b> - HISTORY OF CHANGES - </b>
 *  
 * <table align="left" style="width:800px">
 * <tr><td> Date       </td><td> Software Version </td><td> Initials </td>
 * <td> Description </td></tr>
 * <tr><td> 12.04.2021. 22:13:26 (UTC+01:00) </td><td> 1.0.0 </td><td> YOUR_INITIALS </td>
 * <td> Interface Created </td></tr>
 * </table><br><br>
 * <hr>
 * 
 */
void ICU_moduleCfg(ICU_Modules_t en_ICUModule)
{
    /* Configure the input capture unit mode */
    *(pu16_icuModules[en_ICUModule] + ICU_REG_CON1L_OFFSET) |= 0;
}    
