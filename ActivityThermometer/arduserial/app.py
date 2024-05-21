from tkinter import Button
from tkinter import Frame
from tkinter import Label
from tkinter import Tk
from tkinter.ttk import Combobox, Style

from sensor_serial import BAUDRATES
from sensor_serial import SensorSerial
from utils import find_available_serial_ports
import re

class App(Frame):
    def __init__(self, master, *args, **kwargs)->None:
        Frame.__init__(self, master, *args, **kwargs)
        self.master: Tk = master

        #GUI objects creations
        self.serial_devices_combobox: Combobox = self.create_serial_devices_combobox()
        self.refresh_serial_devices_button : Button = self.create_serial_devices_refresh_button()
        self.baudrate_combobox : Combobox = self.create_baudrate_combobox()
        self.connect_serial_button : Button = self.create_connect_serial_button()
        self.temperature_label : Label = self.create_temperature_label()
        self.read_temperature : Button = self.create_read_temperature_button() 
        self.init_gui()
        #Other objects
        self.sensor_serial : SensorSerial | None = None
        self.init_gui()
        
    
    def init_gui(self,)->None:
        # GUI Config
        self.master.title = 'example'
        self.master.geometry('400x450')
        self['bg'] = '#282c34'
        self.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.refresh_serial_devices_button.grid(row=2, column=0, pady=30, padx=12 )
        self.serial_devices_combobox.grid(row=3, column=0, pady=10, padx=12)
        self.baudrate_combobox.grid(row=4, column=0, pady=10, padx=12)
        self.connect_serial_button.grid(row=5, column=0, pady=25, padx=12)
        self.temperature_label.grid(row=6, column=0, pady=10, padx=12)
        self.read_temperature.grid(row=7, column=0, pady=10, padx=12)

        #Settings
        self.baudrate_combobox.current(0)
        
    def create_serial_devices_combobox(self)->Combobox:
        ports = find_available_serial_ports()
        return Combobox(self, values=ports, font=('Courier',20), style='TCombobox')
    
    def create_serial_devices_refresh_button(self) -> Button:
        return Button(self, 
                      text='Refresh available serial devices',
                      command=self.refresh_serial_devices
        )
    
    def create_baudrate_combobox(self) -> Combobox:
        return Combobox(master = self, 
                        values=BAUDRATES,
                        font=('Arial', 12)
        )

    def create_connect_serial_button(self) -> Button:
        return Button(
            master = self,
            text = 'Connect',
            background='#61afef', 
            foreground='#282c34',
            command = self.create_sensor_serial
        )

    def create_temperature_label(self) -> Label:
        return Label(
            master = self,
            text = 'XX °C',
            font = ('Courier', 20),
            background='#282c34',
            foreground='#ffffff'
        )

    def create_read_temperature_button(self) -> Button:
        return Button(
            master = self,
            text = 'Read temperature',
            background='#61afef', 
            foreground='#282c34',
            command = self.read_temperature,
        )
    
    def refresh_serial_devices(self):
        ports = find_available_serial_ports()
        self.serial_devices_combobox.select_clear()
        self.serial_devices_combobox['values'] = ports
    
    def create_sensor_serial(self) -> SensorSerial:
        port = self.serial_devices_combobox.get()
        baudrate = self.baudrate_combobox.get()

        if port == '' or baudrate == 'Baudrate':
            raise ValueError(f'Incorrect values for {port=} {baudrate=}')
    
        self.sensor_serial = SensorSerial(
            serial_port = port, 
            baudrate = int(baudrate)
        )

    def read_temperature(self) -> None:
        if self.sensor_serial is not None:
            temperature_response = self.sensor_serial.send('TC2')
            temperature = self.extract_temperature(temperature_response)
            self.temperature_label['text'] = f"{temperature} °C"
            return
        raise RuntimeError('Serial connection has not been initialized')

    def extract_temperature(self, response: str) -> str:
        match = re.search(r'(\d+\.\d+)', response)
        if match:
            return match.group(1)
        else:
            raise ValueError('Invalid temperature response')


root = Tk()

if __name__ == '__main__':
    app = App(root)
    root.mainloop()