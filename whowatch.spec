Summary:	whowatch display information about processes and logged users
Name:		whowatch
Version:	1.4
Release:	1
License:	GPL
Group:		Utilities/Console
Group(pl):	Narzêdzia/Konsola
Source0:	%{name}-%{version}.tar.gz
Patch0:		whowatch-utmpx.patch
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%description

Whowatch is an interactive console utility that displays informations about
the users currently logged on to the machine, in real time. 
Besides standard information (login, tty, host, user's process) you can
see type of login (ie. ssh, telnet). You can also see selected user's
processes tree or all system processes tree.
In the process tree mode there is ability to send INT or KILL signal to
selected process.

%prep
%setup -q
%patch0 -p1

%build
./configure --prefix=$RPM_BUILD_ROOT
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
install whowatch $RPM_BUILD_ROOT/%{_bindir}
install whowatch.1 $RPM_BUILD_ROOT/%{_mandir}/man1
gzip -9 $RPM_BUILD_ROOT/%{_mandir}/man1/whowatch.1

%files
%defattr(755,root,root,755)
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
