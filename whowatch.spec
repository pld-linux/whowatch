Summary:	whowatch display information about processes and logged users
Summary(pl):	whowatch wy¶wietla informacje o procesach i zalogowanych u¿ytkownikach
Name:		whowatch
Version:	1.4
Release:	3
License:	GPL
Group:		Applications/Console
Source0:	http://wizard.ae.krakow.pl/~mike/download/%{name}-%{version}.tar.gz
# Source0-md5:	0870155e8b75b99f9954e76fb20f9528
Patch0:		%{name}-utmpx.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.1
URL:		http://wizard.ae.krakow.pl/~mike/#whowatch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Whowatch is an interactive terminal utility that displays informations
about the users currently logged on to the machine, in real time.
Besides standard information (login, tty, host, user's process) you
can see type of login (ie. ssh, telnet). You can also see selected
user's processes tree or all system processes tree. In the process
tree mode there is ability to send INT or KILL signal to selected
process.

%description -l pl
Whowatch jest interaktywnym terminalowym narzêdziem, które wy¶wietla
informacje o aktualnie zalogowanych u¿ytkownikach w czasie
rzeczywistym. Poza standardowymi informacjami (login, tty, host,
user's process) mo¿na zobaczyæ poprzez jak± us³ugê kto¶ sie zalogowa³
(ssh, telnet...). Mo¿na tak¿e zobaczyæ drzewo procesów u¿ytkownika lub
drzewo procesów systemowych. W tym drzewie mo¿liwe jest wysy³anie do
procesów sygna³ów INT lub KILL.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install whowatch $RPM_BUILD_ROOT%{_bindir}
install whowatch.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
