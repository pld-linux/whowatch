Summary:	whowatch display information about processes and logged users
Summary(pl):	whowatch wyswietla informacje o procesach i zalogowanych uzytkownikach
Name:		whowatch
Version:	1.4
Release:	2
License:	GPL
Group:		Utilities/Console
Group(pl):	Narzêdzia/Konsola
Source0:	http://wizard.ae.krakow.pl/~mike/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-utmpx.patch
URL:		http://wizard.ae.krakow.pl/~mike/#whowatch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whowatch is an interactive console utility that displays informations
about the users currently logged on to the machine, in real time.
Besides standard information (login, tty, host, user's process) you
can see type of login (ie. ssh, telnet). You can also see selected
user's processes tree or all system processes tree. In the process
tree mode there is ability to send INT or KILL signal to selected
process.

%description -l pl
Whowatch jest interaktywnym konsolowym narzedziem, ktore wyswietla
informacje o aktualnie zalogowanych uzytkownikach w czasie rzeczywistym.
Poza standardowymi informacjami (login, tty, host, user's process)
mozna zobaczyc sposob w jaki login sie odbyl (ssh, telnet...). Mozna
takze zobaczyc drzewo procesow uzytkownika lub drzewo procesow 
systemowych. W tym drzewie mozliwe jest wysylanie do procesow 
sygnalow INT lub KILL.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install whowatch $RPM_BUILD_ROOT/%{_bindir}
install whowatch.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
