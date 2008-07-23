%define name	cd-mason
%define version	0.1
%define release %mkrel 4

Name: 	 	%{name}
Summary: 	Simple CD burning interface for GNOME
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-0.1-datadir.patch.bz2
URL:		http://cd-mason.berlios.de/
License:	GPL
Group:		Archiving/Cd burning
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig ImageMagick
BuildRequires:	libgnome-vfs2-devel gtk2-devel
Requires:	cdrecord mkisofs madplay vorbis-tools

%description
CD-Mason is yet another GUI frontend for cdrecord and mkisofs. It tries to
make CD burning on Linux and other POSIX platforms as easy as possible. It
has been designed with novice desktop users in mind (think Aunt Tillie) that
don't want to know about burning modes, sector sizes, ISO-9660 images or
even the difference between an MP3 and a WAV music file. All these subtleties
should be handled transparently using a simple drag'n'drop interface.

%prep
%setup -q
%patch -p1

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir -p %buildroot/%_datadir/%name
cp src/*.svg src/*.png %buildroot/%_datadir/%name/

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CD-Mason
Comment=Simple, powerful CD burning
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
Categories=GNOME;GTK;X-MandrivaLinux-System-Archiving-CDBurning;AudioVideo;DiscBurning;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 src/%name.svg $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 src/%name.svg $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 src/%name.svg $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

