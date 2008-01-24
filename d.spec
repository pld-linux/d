Summary:	D - The Directory Lister
Summary(pl.UTF-8):	D - wyświetlacz katalogów
Name:		d
Version:	1.2.0
Release:	4
License:	GPL v2+
Group:		Applications/System
Source0:	http://pages.xtn.net/~ecogburn/%{name}-%{version}.tar.bz2
# Source0-md5:	7ce4ee18fd220588eab2c798e22b76a6
Patch0:		%{name}-opt.patch
Patch1:		%{name}-types.patch
Patch2:		%{name}-info.patch
URL:		http://pages.xtn.net/~ecogburn/d.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
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

%description -l pl.UTF-8
D jest alternatywą dla ls i jego długiego wyjścia. Optymalizuje
wyjście by uzyskać więcej miejsca na nazwę plików i redukuje
prawdopodobieństwo zawinięcia listingu. Posiada także opcję
--dirs-first wypisującą zawsze katalogi przed normalnymi plikami
niezależnie od aktualnie ustawionych opcji sortowania. Pozwala na
pliki konfiguracyjne w systemie oraz na koncie użytkownika,
pozwalające ustawić kilkanaście opcji dostępnych z linii poleceń, 
jak także opcję color pozwalającą całkowicie zmienić kolory wyjście,
podobnie jak w ls, ale w bardziej wygodnym pliku konfiguracyjnym.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub .
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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_infodir}/%{name}*
