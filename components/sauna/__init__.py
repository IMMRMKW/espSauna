################################################
 # Air purifier in ESPHome                      #
 #	                                            #
 # Authors: groothuisss & IMMRMKW               #
 ################################################
 
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import sensor

from esphome import components
#from airpurifier import CONFIG_SCHEMA
from esphome.const import (
    CONF_ID,
)

CONF_SENSOR_TEMP = "temperature_sensor"
CONF_SENSOR_HUMID = "humidity_sensor"
CONF_HEATER_PIN = "fan_pwm_pin"
CONF_HUMIDIFIER_PIN = "fan_tacho_pin"


sauna_ns = cg.esphome_ns.namespace('sauna')
Sauna = sauna_ns.class_('Sauna', cg.Component)

AUTO_LOAD = ["waterpump"]

CONFIG_SCHEMA = cv.Schema(
    {
    cv.GenerateID(): cv.declare_id(Sauna),
    cv.Optional(CONF_SENSOR_TEMP): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_HUMID_SENSOR): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_HEATER_PIN): cv.All(pins.internal_gpio_input_pin_schema),
    cv.Optional(CONF_HUMIDIFIER_PIN): cv.All(pins.internal_gpio_input_pin_schema),
    })





async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    if CONF_SENSOR_TEMP in config:
        sens = await cg.get_variable(config[CONF_SENSOR_TEMP])
        cg.add(var.set_sensor_temperature(sens))

    if CONF_SENSOR_HUMID in config:
        sens = await cg.get_variable(config[CONF_SENSOR_HUMID])
        cg.add(var.set_sensor_humidity(sens))

    if CONF_HEATER_PIN in config:
        power_en_pin = await cg.gpio_pin_expression(config[CONF_POWER_EN_PIN])
        cg.add(var.set_power_en_pin(power_en_pin))

    if CONF_HUMIDIFIER_PIN in config:
        power_pwm_pin = await cg.gpio_pin_expression(config[CONF_POWER_PWM_PIN])
        cg.add(var.set_power_pwm_pin(power_pwm_pin))