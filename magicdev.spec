%define		snap	20030922

Summary:	User-space device-watching daemon that runs within the GNOME desktop.
Name:		magicdev
Version:	1.1.4
Release:	1.%{snap}.1
License:	GPL
Group:		Daemons
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	47d43420f03bf9acbbbbcab408d2e781
Patch0:		%{name}-default-dvd-player.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	libtool
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	ORBit2-devel >= 2.8.1
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	rpm-build >= 4.1-10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User-space device-watching daemon that runs within the GNOME desktop.
Some features include:
- Auto-mounting removeable media on insertion
- Launching a given command when an audio CD is inserted.


%prep
%setup -q -n %{name}
%patch0 -p1

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
