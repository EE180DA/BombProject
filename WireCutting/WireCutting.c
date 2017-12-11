#include <mraa.h>
#include <signal.h>
#include <stdlib.h>

sig_atomic_t volatile run_flag = 1;

void sig_handler(int sig)
{
	if (sig == SIGINT)
		run_flag = 0;
}

void BOOM(int value)
{
	value = 0;
}

int main()
{
	mraa_aio_context adc_a0;
	uint16_t adc_value = 0;
	float adc_value_float = 0.0;
	mraa_result_t r = MRAA_SUCCESS;
	adc_a0 = mraa_aio_init(0);
	if (adc_a0 == NULL) {
		return 1;
	}
	srand(time(NULL));
	int rando = rand() %5;
	//signal(SIGINT, sig_handler);

	/*while (run_flag) {
		adc_value = mraa_aio_read(adc_a0);
	        adc_value_float = mraa_aio_read_float(adc_a0);
	        fprintf(stdout, "V: %f\n", adc_value_float);
	}*/

	adc_value = mraa_aio_read(adc_a0);
	adc_value_float = mraa_aio_read_float(adc_a0);
	
	if (rando == 0)
	{
		fprintf(stdout, "Cut Red/White wire!\n");
		while (adc_value_float > 0.313f && adc_value_float < 0.319f)
		{
			adc_value = mraa_aio_read(adc_a0);
	        	adc_value_float = mraa_aio_read_float(adc_a0);
			if (adc_value_float < 0.313f || adc_value_float > 0.319f)
			{
				if (adc_value_float > 0.458f && adc_value_float < 0.462f)
				{
					fprintf(stdout, "SUCCESS!\n");
				}
				else
				{
					fprintf(stdout, "BOOM!\n");
				}
			}	
		}
	}
	else if (rando == 1)
	{
		fprintf(stdout, "Cut Brown/Green wire!\n");
		while (adc_value_float > 0.313f && adc_value_float < 0.319f)
		{
			adc_value = mraa_aio_read(adc_a0);
	        	adc_value_float = mraa_aio_read_float(adc_a0);
			if (adc_value_float < 0.313f || adc_value_float > 0.319f)
			{
				if (adc_value_float > 0.368f && adc_value_float < 0.372f)
				{
					fprintf(stdout, "SUCCESS!\n");
				}
				else
				{
					fprintf(stdout, "BOOM!\n");
				}
			}			
		}
	}
	else if (rando == 2)
	{
		fprintf(stdout, "Cut Brown/Blue wire!\n");
		while (adc_value_float > 0.313f && adc_value_float < 0.319f)
		{
			adc_value = mraa_aio_read(adc_a0);
	        	adc_value_float = mraa_aio_read_float(adc_a0);
			if (adc_value_float < 0.313f || adc_value_float > 0.319f)
			{
				if (adc_value_float > 0.347f && adc_value_float < 0.352f)
				{
					fprintf(stdout, "SUCCESS!\n");
				}
				else
				{
					fprintf(stdout, "BOOM!\n");
				}
			}			
		}
	}
	else if (rando == 3)
	{
		fprintf(stdout, "Cut Red/Red wire!\n");
		while (adc_value_float > 0.313f && adc_value_float < 0.319f)
		{
			adc_value = mraa_aio_read(adc_a0);
	        	adc_value_float = mraa_aio_read_float(adc_a0);
			if (adc_value_float < 0.313f || adc_value_float > 0.319f)
			{
				if (adc_value_float > 0.340f && adc_value_float < 0.344f)
				{
					fprintf(stdout, "SUCCESS!\n");
				}
				else
				{
					fprintf(stdout, "BOOM!\n");
				}
			}			
		}
	}
	else if (rando == 4)
	{
		fprintf(stdout, "Cut Black/Black wire!\n");
		while (adc_value_float > 0.313f && adc_value_float < 0.319f)
		{
			adc_value = mraa_aio_read(adc_a0);
	        	adc_value_float = mraa_aio_read_float(adc_a0);
			if (adc_value_float < 0.313f || adc_value_float > 0.319f)
			{
				if (adc_value_float > 0.335f && adc_value_float < 0.3395f)
				{
					fprintf(stdout, "SUCCESS!\n");
				}
				else
				{
					fprintf(stdout, "BOOM!\n");
				}
			}			
		}
	}	
	
	r = mraa_aio_close(adc_a0);
	if (r != MRAA_SUCCESS) {
	        mraa_result_print(r);
	}
	return r;
}
