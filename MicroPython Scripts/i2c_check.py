import machine 

pico_I2C0 = 0
i2c = machine.I2C(pico_I2C0, 
                  scl=machine.Pin(17), 
                  sda=machine.Pin(18),
                  freq=400000)

devices = i2c.scan()

if devices:
    for device in devices:
        print(hex(device))
        

def reg_write(i2c, addr, reg, data):
    msg = bytearray()
    msg.append(data)
    
    i2c.writeto_mem(addr, reg, msg)
    
def reg_read(i2c, addr, reg, nbytes=1):
    if nbytes < 1:
        return bytearray()

    data = i2c.readfrom_mem(addr, reg, nbytes)
    return data

data = reg_read(i2c,
                device_addr,
                reg_dev_id)
