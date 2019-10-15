/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   libft.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: tmarx <marvin@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/08 12:09:33 by tmarx             #+#    #+#             */
/*   Updated: 2019/10/12 18:30:37 by tmarx            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef LIBFT_H

# define LIBFT_H
# include <unistd.h>
# include <string.h>
# include <stdlib.h>

typedef struct	s_list
{
	void			*content;
	struct s_list	*next;
}				t_list;
int				ft_atoi(const char *str);
int				ft_isalpha(int c);
int				ft_isdigit(int c);
int				ft_isalnum(int c);
int				ft_isascii(int c);
int				ft_isprint(int c);
int				ft_toupper(int c);
int				ft_tolower(int c);
void			ft_putchar_fd(char c, int fd);
void			ft_putnbr_fd(int nb, int fd);
void			ft_putstr_fd(const char *str, int fd);
int				ft_strncmp(const char *s1, const char *s2, size_t n);
char			*ft_strcpy(char *dest, const char *src);
char			*ft_strdup(const char *src);
size_t			ft_strlcat(char *dest, const char *src, size_t size);
size_t			ft_strlen(const char *str);
char			*ft_strchr(const char *s, int c);
char			*ft_strrchr(const char *s, int c);
char			*ft_strnstr(const char *str, const char *to_find, size_t len);
void			*ft_memset(void *b, int c, size_t len);
void			ft_bzero(void *b, size_t n);
void			*ft_memcpy(void *dst, const void *src, size_t n);
void			*ft_memccpy(void *dst, const void *src, int c, size_t n);
void			*ft_memmove(void *dst, const void *src, size_t len);
void			*ft_memchr(const void *s, int c, size_t n);
int				ft_memcmp(const void *s1, const void *s2, size_t n);
void			ft_putendl_fd(char const *s, int fd);
char			*ft_itoa(int nbr);
char			*ft_substr(char const *s, unsigned int start, size_t len);
char			*ft_strjoin(char const *s1, char const *s2);
char			*ft_strtrim(char const *s1, char const *set);
t_list			*ft_lstnew(void *content);
void			ft_lstadd_front(t_list **list, t_list *new);
void			ft_lstadd_back(t_list **list, t_list *new);
int				ft_lstsize(t_list *list);
t_list			*ft_lstlast(t_list *list);
void			ft_lstdelone(t_list *alst, void (*del)(void *));
void			ft_lstclear(t_list **list, void (*del)(void *));
void			ft_lstiter(t_list *list, void (*f)(void *));
t_list			*ft_lstmap(t_list *list, void *(*f)(void *));
void			*ft_calloc(size_t nmenb, size_t size);
char			**ft_split(char const *s, char c);
size_t			ft_strlcpy(char *dest, const char *src, size_t dstsize);
char			*ft_strmapi(char const *s, char (*f)(unsigned int, char));
#endif
