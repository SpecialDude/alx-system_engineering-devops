#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Loops infinitely
 *
 * Return: zero but goodluck breaking from the loop
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Program entry point. Creates 5 zombie processes
 *
 * Return: zero
 */
int main(void)
{
	pid_t zombie;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();

		if (zombie == 0)
			return (0);

		printf("Zombie process created, PID: %d\n", zombie);
	}

	infinite_while();

	return (0);
}
