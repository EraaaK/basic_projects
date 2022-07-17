import wmi


def MachineInfos():
    c = wmi.WMI()
    my_system = c.Win32_ComputerSystem()[0]

    marca = str({my_system.Manufacturer})
    modelo = str({my_system.Model})
    nome = str({my_system.Name})
    qtd_cpus = str({my_system.NumberOfProcessors})
    arquitetura = str({my_system.SystemType})
    familia = str({my_system.SystemFamily})

    pc_info = []
    pc_info.append(marca)
    pc_info.append(modelo)
    pc_info.append(nome)
    pc_info.append(qtd_cpus)
    pc_info.append(arquitetura)
    pc_info.append(familia)

    print('PING')

    return pc_info
