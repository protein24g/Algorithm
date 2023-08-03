#include<stdio.h>
#include<string.h>

int main(void)
{
	int t, temp[501] = { 0 };
	int q[501] = { 0 }, d[501] = { 0 }, n[501] = { 0 }, p[501] = { 0 };

	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%d", &temp[i]);
	}
	for (int i = 0; i < t; i++)
	{
		while(temp[i] != 0)
		if (temp[i] >= 25)
		{
			temp[i] -= 25;
			q[i]++;
		}
		else if (temp[i] >= 10)
		{
			temp[i] -= 10;
			d[i]++;
		}
		else if (temp[i] >= 5)
		{
			temp[i] -= 5;
			n[i]++;
		}
		else if (temp[i] >= 1)
		{
			temp[i] -= 1;
			p[i]++;
		}
	}

	for (int i = 0; i < t; i++)
	{
		printf("%d %d %d %d\n", q[i], d[i], n[i], p[i]);
	}
}