AC_INIT([php-mincrypt], [0.0.4], [mignov@gmail.com])
AC_CONFIG_MACRO_DIR([m4])
AM_INIT_AUTOMAKE([-Wall -Werror])
#AM_INIT_AUTOMAKE([-Wno-portability])

AC_CHECK_LIB([mincrypt], [mincrypt_get_version], [], AC_MSG_ERROR([You need libmincrypt to compile this app]))
AC_CHECK_TOOL([MKDIR], [mkdir])
AC_CHECK_TOOL([ECHO], [echo])
AC_CHECK_TOOL([RM], [rm])
AC_CHECK_TOOL([CP], [cp])
AC_CHECK_TOOL([PHPCONFIG], [php-config])

#AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile src/Makefile tests/Makefile])
AC_OUTPUT
