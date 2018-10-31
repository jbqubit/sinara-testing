# This is an example device database that needs to be adapted to your setup.
# The list of devices here is not exhaustive.

core_addr = "128.8.195.91"


device_db = {
    "core": {
        "type": "local",
        "module": "artiq.coredevice.core",
        "class": "Core",
        "arguments": {"host": core_addr, "ref_period": 1e-9}
    },
    "core_log": {
        "type": "controller",
        "host": "::1",
        "port": 1068,
        "command": "aqctl_corelog -p {port} --bind {bind} " + core_addr
    },
    "core_cache": {
        "type": "local",
        "module": "artiq.coredevice.cache",
        "class": "CoreCache"
    },
    "core_dma": {
        "type": "local",
        "module": "artiq.coredevice.dma",
        "class": "CoreDMA"
    },

    "i2c_switch0": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "PCA9548",
        "arguments": {"address": 0xe0}
    },
    "i2c_switch1": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "PCA9548",
        "arguments": {"address": 0xe2}
    }
}

device_db["mynovatech"] = {
	"type": "controller",
        "host": "::1",
        "port": 3254,
        "command": "aqctl_novatech409b --simulation "
        "-p {port} --bind {bind}"
    }

for i in range(4):
    s = "ttl" + str(i)
    device_db[s] = {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLInOut",
        "arguments": {"channel": i},
    }

for i in range(20):
    device_db["ttl" + str(i+4)] = {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": i+4}
    }

device_db.update(
    {
        "spi_novogorny0": {
            "type": "local",
            "module": "artiq.coredevice.spi2",
            "class": "SPIMaster",
            "arguments": {"channel": 24}
        },
        "ttl_novogorny0_cnv": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 25}
        },
        "novogorny0" : {
            "type": "local",
            "module": "artiq.coredevice.novogorny",
            "class": "Novogorny",
            "arguments": {
                "spi_device": "spi_novogorny0",
                "cnv_device": "ttl_novogorny0_cnv",
            }
        },
        "urukul0_cpld": {
            "type": "local",
            "module": "artiq.coredevice.urukul",
            "class": "CPLD",
            "arguments": {
                "spi_device": "spi_urukul0",
                "io_update_device": "ttl_urukul0_io_update",
                "refclk": 125e6,
                "clk_sel": 1,
                "sync_sel": 0
            }
        },
        "spi_urukul0": {
            "type": "local",
            "module": "artiq.coredevice.spi2",
            "class": "SPIMaster",
            "arguments": {"channel": 26}
        },
        "ttl_urukul0_io_update": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 27}
        }
    }
)

for i in range(4):
    device_db["ttl_urukul0_sw" + str(i)] = {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": i + 28}
        }
    device_db["urukul0_ch" + str(i)] = {
            "type": "local",
            "module": "artiq.coredevice.ad9910",
            "class": "AD9910",
            "arguments": {
                "pll_n": 32,  # for 125 MHz clock
                "chip_select": i + 4,
                "cpld_device": "urukul0_cpld",
                "sw_device": "ttl_urukul0_sw" + str(i)
        }
    }

device_db.update(
    {
        "led0": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 32}
        },
        "led1": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 33}
        },
        "spi_zotino0": {
            "type": "local",
            "module": "artiq.coredevice.spi2",
            "class": "SPIMaster",
            "arguments": {"channel": 36}
        },
        "ttl_zotino0_ldac": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 37}
        },
        "ttl_zotino0_clr": {
            "type": "local",
            "module": "artiq.coredevice.ttl",
            "class": "TTLOut",
            "arguments": {"channel": 38}
        },
        "zotino0": {
            "type": "local",
            "module": "artiq.coredevice.zotino",
            "class": "Zotino",
            "arguments": {
                "spi_device": "spi_zotino0",
                "ldac_device": "ttl_zotino0_ldac",
                "clr_device": "ttl_zotino0_clr"
            }
        },
        "pmt": "ttl0",
        "ionization_shutter": "ttl18", # open SRS shutter for photoionization
        "dop_shutter": "ttl17", # open SRS shutter for far detuned doppler cooling
        "dop_near": "ttl16",  # turn on AOM for near resonant doppler cooling
        "pump_ds": "ttl15",  # fiber AOM 935 nm
        "t0": "ttl7"  # start of experiments
    }
)

