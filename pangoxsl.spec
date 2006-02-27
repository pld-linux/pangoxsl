Summary:	Additional XSL properties for Pango
Summary(pl):	Dodatkowe w�a�ciwo�ci XSL dla Pango
Name:		pangoxsl
Version:	1.6.0.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/pangopdf/%{name}-%{version}.tar.gz
# Source0-md5:	6a389e32feaa8210222a1f3c373d5a99
URL:		http://pangopdf.sourceforge.net/
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	pango-devel >= 1.6
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional XSL properties for Pango.

%description -l pl
Dodatkowe w�a�ciwo�ci XSL dla Pango.

%package devel
Summary:	Header files for pangoxsl library
Summary(pl):	Pliki nag��wkowe biblioteki pangoxsl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pango-devel >= 1.6

%description devel
Header files for pangoxsl library.

%description devel -l pl
Pliki nag��wkowe biblioteki pangoxsl.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libpangoxsl-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangoxsl-*.so
%{_libdir}/libpangoxsl-*.la
%{_includedir}/pangoxsl
%{_pkgconfigdir}/pangoxsl.pc
%{_gtkdocdir}/pangoxsl