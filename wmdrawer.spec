Summary:	wmDrawer - a dock application which provides a retractable button bar
Summary(pl):	Dokowalna aplikacja wysuwaj±cych siê guzików
Name:		wmdrawer
Version:	0.10.4
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://people.easter-eggs.org/~valos/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	34dd26a740074794a45e2aed0e00454a
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

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -pipe -Wall -pedantic `pkg-config --cflags gdk-pixbuf-xlib-2.0`" \
	USE_GDKPIXBUF2="1" \
	USE_GDKPIXBUF="0"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README wmdrawerrc.example
%attr(755,root,root) %{_bindir}/%{name}
