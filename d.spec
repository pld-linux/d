Summary:	D - The Directory Lister
Summary(pl):	D - wy¶wietlacz katalogów
Name:		d
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://pages.xtn.net/~ecogburn/%{name}-%{version}.tar.bz2
# Source0-md5:	7ce4ee18fd220588eab2c798e22b76a6
URL:		http://pages.xtn.net/~ecogburn/d.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D is an alternative to ls and its long format output. It optimizes the
output to create more space for the filename and reduce the chance of
wrap around. It also has a --dirs-first option to always print
directories before regular files regardless of the current sort
option. Those familiar with Midnight Commander will recognize this
behavior. It allows for system and user configuration files, which can
specify several options that are available on the command line, as
well as the 'color' option which can be used to completely customize
the colorization of output, like ls but in a more convenient
configuration file.

%description -l pl
D jest alternatyw± dla ls i jego d³ugiego wyj¶cia. Optymalizuje
wyj¶cie by uzyskaæ wiêcej miejsca na nazwê plików i redukuje
prawdopodobieñstwo zawiniêcia listingu. Posiada tak¿e opcjê
--dirs-first wypisuj±c± zawsze katalogi przed normalnymi plikami
niezale¿nie od akutalnie ustawionych opcji sortowania. Pozwala na
pliki konfiguracyjne w systemie oraz na koncie u¿ytkownika,
pozwalaj±ce ustawiæ kilkana¶cie opcji dostêpnych z lini poleceñ, jak
tak¿e opcjê color pozwalaj±c± ca³kowicie zmieniæ kolory wyjscie,
podobnie jak w ls, ale w bardziej wygodnym pliku konfiguracyjnym.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/%{name}*
