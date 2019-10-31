#include <stdio.h>
#include <stdlib.h>
#include "$$1libft.h"

char map(unsigned int i, char c)
{
    (void)i;
	return ((char) (c + 3));
}

void del(void *content)
{
	(void) content;
}

void *lstmap(void *content)
{
	(void) content;
	return ft_calloc(sizeof(char), 1);
}

int main()
{
$$2
    return (0);
}
