Summary:	wmDrawer - a dock application which provides a retractable button bar
Summary(pl):	Dokowalna aplikacja wysuwaj±cych siê guzików
Name:		wmdrawer
Version:	0.10.5
Release:	2
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://people.easter-eggs.org/~valos/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	b8c4a5d5abd593a29504dfe4c30c8925
Source1:	%{name}.desktop
Patch0:		%{name}-lib64.patch
URL:		http://people.easter-eggs.org/~valos/wmdrawer/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmDrawer is a dock application (dockapp) which provides a drawer
(retractable button bar) to launch applications.

%description -l pl
wmDrawer jest dokowaln± aplikacj± dla WindowMakera, która wy¶wietla
³adne menu z guzikami do uruchamiania aplikacji.

%prep
%setup -q
%if "%{_lib}" == "lib64"
%patch0 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -pipe -Wall -pedantic `pkg-config --cflags gdk-pixbuf-xlib-2.0`" \
	USE_GDKPIXBUF2="1" \
	USE_GDKPIXBUF="0"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}
install -d $RPM_BUILD_ROOT%{_mandir}/man1

install %{name} $RPM_BUILD_ROOT%{_bindir}
install doc/%{name}.1* $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO wmdrawerrc.example
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/*
%{_mandir}/man1/*
