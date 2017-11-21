#include <mraa/i2c.h>

#define RGB_ADDRESS (0xc4 >> 1)
#define LCD_ADDRESS (0x7c >> 1)

#define REG_MODE1 0x00
#define REG_MODE2 0x01
#define REG_OUTPUT 0x08

#define REG_RED 0x04
#define REG_GREEN 0x03
#define REG_BLUE 0x02
#define LCD_SETCGRAMADDR 0x40
#define LCD_FUNCTIONSET 0x20
#define LCD_CLEARDISPLAY 0x01
#define LCD_DISPLAYCONTROL 0x08
#define LCD_DISPLAYON 0x04
#define LCD_DISPLAY OFF 0x00
#define LCD_CURSORON 0x02
#define LCD_CURSOROFF 0x00
#define LCD_BLINKON 0x01
#define LCD_BLINKOFF 0x00

uint8_t _displayfunction;
uint8_t _displaycontrol;
uint8_t _displaymode;
uint8_t timer = 15;


void rgb_command(mraa_i2c_context rgb_i2c, uint8_t addr, uint8_t dta)
{
	uint8_t to_send[2] = {addr, dta};
	mraa_i2c_write(rgb_i2c, to_send, 2);
}
void command(mraa_i2c_context lcd_i2c,uint8_t addr, uint8_t value)
{
	unsigned char dta[2]={addr,value};
	mraa_i2c_write(lcd_i2c,dta,2);
}
void set_RGB_color(mraa_i2c_context rgb_i2c, uint8_t r, uint8_t g, uint8_t b)
{
	rgb_command(rgb_i2c, REG_RED, r);
	rgb_command(rgb_i2c, REG_GREEN, g);
	rgb_command(rgb_i2c, REG_BLUE, b);
}
void setCursor(mraa_i2c_context lcd_i2c, uint8_t col, uint8_t row)
{
	col = (row == 0 ? col|0x80 : col|0xc0);
	unsigned char dta[2]={0x80,col};
	mraa_i2c_write(lcd_i2c,dta,2);
}

int main()
{
	usleep(50000);
	//setup mraa
	mraa_i2c_context rgb_i2c;
	mraa_init();
	rgb_i2c = mraa_i2c_init(0);
	mraa_i2c_address(rgb_i2c, RGB_ADDRESS);
	mraa_i2c_context lcd_i2c;
	mraa_init();
	lcd_i2c = mraa_i2c_init(1);
	mraa_i2c_address(lcd_i2c, LCD_ADDRESS);	
	
	_displayfunction |= 0x08;//LCD 2 Line mode
	//Send function set command sequence
	command(lcd_i2c,0x80, LCD_FUNCTIONSET | _displayfunction);
	usleep(4500);
	command(lcd_i2c,0x80, LCD_FUNCTIONSET | _displayfunction);
	usleep(150);
	command(lcd_i2c,0x80, LCD_FUNCTIONSET | _displayfunction);
	command(lcd_i2c,0x80, LCD_FUNCTIONSET | _displayfunction);
	//Turn on display with no cursor or blinking
	_displaycontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF;
	//Display On
	_displaycontrol |= LCD_DISPLAYON;
	command(lcd_i2c,0x80, LCD_DISPLAYCONTROL | _displaycontrol);
	command(lcd_i2c,0x80, LCD_CLEARDISPLAY); //Clear Display
	usleep(2000);
	
	_displaymode = 0x02|0x00; //Initialize to default text direction
	command(lcd_i2c,0x80, 0x04 | _displaymode); //set entry mode

	rgb_command(rgb_i2c, REG_MODE1, 0); //backlight init
	rgb_command(rgb_i2c, REG_OUTPUT,0xFF);
	rgb_command(rgb_i2c, REG_MODE2, 0x20);
	//backlight color
	set_RGB_color(rgb_i2c, 255, 255, 255); 
//Game active state (timer>0)
while (timer>0)
{
	//first line
	setCursor(lcd_i2c, 0,0);
	command(lcd_i2c, 0x40, ((timer/10)%10)+48); //10th digit of timer
	command(lcd_i2c, 0x40, (timer%10)+48); //1st digit of timer
	command(lcd_i2c, 0x40, ' '); 
	command(lcd_i2c, 0x40, 'S');  
	command(lcd_i2c, 0x40, 'T'); 
	command(lcd_i2c, 0x40, 'A' ); 
	command(lcd_i2c, 0x40, 'Y'); 
	command(lcd_i2c, 0x40, ' '); 
	command(lcd_i2c, 0x40, 'C'); 
	command(lcd_i2c, 0x40, 'H'); 
	command(lcd_i2c, 0x40, 'I');
	command(lcd_i2c, 0x40, 'L'); 
	command(lcd_i2c, 0x40, 'L');
	command(lcd_i2c, 0x40, ' '); 
	command(lcd_i2c, 0x40, '&');
	command(lcd_i2c, 0x40, ' ');
	//second line
	setCursor(lcd_i2c,0,1); 
	command(lcd_i2c, 0x40, 'N');
	command(lcd_i2c, 0x40, 'O');
	command(lcd_i2c, 0x40, ' ');
	command(lcd_i2c, 0x40, 'O');
	command(lcd_i2c, 0x40, 'N');
	command(lcd_i2c, 0x40, 'E');
	command(lcd_i2c, 0x40, ' ');
	command(lcd_i2c, 0x40, 'G');
	command(lcd_i2c, 0x40, 'O');
	command(lcd_i2c, 0x40, 'E');
	command(lcd_i2c, 0x40, 'S');
	command(lcd_i2c, 0x40, ' ');
	command(lcd_i2c, 0x40, 'B');
	command(lcd_i2c, 0x40, 'O');
	command(lcd_i2c, 0x40, 'O');
	command(lcd_i2c, 0x40, 'M');
	usleep(1000000);
	timer--;
}
//Game over state (timer is 0)
command(lcd_i2c,0x80,LCD_CLEARDISPLAY);
usleep(2000);
command(lcd_i2c,0x40,48);
command(lcd_i2c,0x40,48);
command(lcd_i2c,0x40,' '); 
command(lcd_i2c,0x40,'B');
command(lcd_i2c,0x40,'O');
command(lcd_i2c,0x40,'O');
command(lcd_i2c,0x40,'M');
command(lcd_i2c,0x40,'!');
}
