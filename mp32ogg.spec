%define fver 0.11-8

Name:		mp32ogg
Version:	0.11
Release:	%mkrel 15

Summary:	Convert mp3 music files to ogg music files
License:	Artistic
Group:		Sound
# Author: Nathan Walp <faceprint@faceprint.com>
Url:		http://packages.debian.org/unstable/sound/mp32ogg
Source0:	mp32ogg_%{fver}.tar.bz2
Patch0:     mp32ogg-0.11-force-filename-stringification.mp3

BuildRequires: perl
BuildRequires: perl(MP3::Info)
BuildRequires: perl(String::ShellQuote)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires: mpg123
Requires: perl
Requires: vorbis-tools

%description
Perl script to convert MP3 files into Ogg Vorbis format. It is able to
read ID3 tags from MP3 files and correctly tag the Ogg files, as well as
optionally rename them based on those tags.

%prep
%setup -q -n %name
# fix https://qa.mandriva.com/show_bug.cgi?id=53477
%patch0 -p0

%install
rm -rf %{buildroot}

install -m 755 -D %name  %{buildroot}%{_bindir}/%{name}
perl -c  %{buildroot}%{_bindir}/%{name}

echo -e "%{name}\n\nAuthor: Nathan Walp <faceprint@faceprint.com>\nLicense: Artistic\n" > README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.11-14mdv2011.0
+ Revision: 666485
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-13mdv2011.0
+ Revision: 606658
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11-12mdv2010.1
+ Revision: 523361
- rebuilt for 2010.1

* Wed Sep 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.11-11mdv2010.0
+ Revision: 435646
- forgot to commit patch
- fix 53477

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.11-10mdv2010.0
+ Revision: 426164
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.11-9mdv2009.0
+ Revision: 223316
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.11-7mdv2008.1
+ Revision: 153231
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 09 2007 Götz Waschk <waschk@mandriva.org> 0.11-6mdv2008.0
+ Revision: 60747
- switch to the Debian fork


* Wed Feb 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.11-5mdv2007.0
+ Revision: 123640
- rebuild
- Import mp32ogg

* Mon Sep 06 2004 Michael Scherer <misc@mandrake.org> 0.11-4mdk
- Rebuild
- use %%doc
- remove Packager tag
- use perl-autorequires

