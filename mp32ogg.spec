%define fver 0.11-8

Name:		mp32ogg
Version:	0.11
Release:	%mkrel 13

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
