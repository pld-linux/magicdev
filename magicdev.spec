%define		snap	20030922

Summary:	User-space device-watching daemon that runs within the GNOME desktop
Summary(pl):	Demon ¶ledz±cy urz±dzenia dzia³aj±cy na pulpicie GNOME
Name:		magicdev
Version:	1.1.4
Release:	1.%{snap}.1
License:	GPL
Group:		Applications/System
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	47d43420f03bf9acbbbbcab408d2e781
Patch0:		%{name}-default-dvd-player.patch
Patch1:		%{name}-blacklist.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.26
BuildRequires:	gettext
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.2.0
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
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

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
%{_datadir}/control-center-2.0/capplets/gnome-cd-properties.desktop
%{_datadir}/%{name}/*.glade
