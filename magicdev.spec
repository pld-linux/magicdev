Summary:	User-space device-watching daemon that runs within the GNOME desktop
Summary(pl):	Demon ¶ledz±cy urz±dzenia dzia³aj±cy na pulpicie GNOME
Name:		magicdev
Version:	1.1.6
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	ed2c3ea0258317b1760107475205fc77
Patch0:		%{name}-default-dvd-player.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.4.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires:	gnome-mime-data
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User-space device-watching daemon that runs within the GNOME desktop.
Some features include:
- Auto-mounting removeable media on insertion
- Launching a given command when an audio CD is inserted.

%description -l pl
Uruchamiany w przestrzeni u¿ytkownika demon ¶ledz±cy urz±dzenia
dzia³aj±cy na pulpicie GNOME. Jego mo¿liwo¶ci obejmuj±:
- automontowanie zmienialnych no¶ników po w³o¿eniu
- uruchamianie podanego polecenia po w³o¿eniu p³yty d¼wiêkowej CD.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po

%build
rm -f missing
%{__aclocal}
%{__libtoolize}
intltoolize --copy --force
glib-gettextize --copy --force
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets
mv -f $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop \
	$RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/gnome/capplets/gnome-cd-properties.desktop
%{_datadir}/%{name}
