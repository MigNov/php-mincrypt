NAME=php-mincrypt
PHPINC=`$(PHPCONFIG) --includes`
PHPEDIR=`$(PHPCONFIG) --extension-dir`
PHPCDIR=`$(PHPCONFIG) --configure-options | sed -n 's|.*--with-config-file-scan-dir=\([^ ]*\).*|\1|p'`
MINCRYPT_LIBS=-lmincrypt

EXTRA_DIST = php-mincrypt.c php-mincrypt.h

all: build clean-temp

build:
	$(CC) -Wall -fPIC -DCOMPILE_DL_MINCRYPT=1 $(PHPINC) -c -o $(NAME).o php-mincrypt.c
	$(CC) -Wall -fPIC -shared $(LIBS) -rdynamic -o $(NAME).so $(NAME).o $(MINCRYPT_LIBS)
	$(ECHO) "Extension compiled as $(NAME).so"

install-exec-local:
	mkdir -p $(DESTDIR)$(PHPEDIR)
	$(CP) $(NAME).so $(DESTDIR)$(PHPEDIR)
	mkdir -p $(DESTDIR)$(PHPCDIR)
	$(RM) -f $(DESTDIR)$(PHPCDIR)/$(NAME).ini
	echo "extension=$(NAME).so" > $(DESTDIR)$(PHPCDIR)/$(NAME).ini


uninstall-local:
	$(RM) -f $(DESTDIR)$(PHPCDIR)/$(NAME).ini
	$(RM) -f $(DESTDIR)$(PHPEDIR)/$(NAME).so

clean-temp:
	$(RM) -f *.o
