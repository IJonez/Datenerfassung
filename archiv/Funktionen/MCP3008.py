def read_MCP3008(channel=0):
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return(data)
