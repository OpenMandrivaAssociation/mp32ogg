%define fver 0.11-8
Summary:	Convert mp3 music files to ogg music files
Name:		mp32ogg
Version:	0.11
Release:	%mkrel 9
License:	Artistic
Url:		http://packages.debian.org/unstable/sound/mp32ogg
Group:		Sound
Source0:	mp32ogg_%{fver}.tar.bz2
Requires:	perl mpg123 vorbis-tools
BuildRequires:	perl perl-MP3-Info perl-String-ShellQuote
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# Author: Nathan Walp <faceprint@faceprint.com>

%description
Perl script to convert MP3 files into Ogg Vorbis format. It is able to
read ID3 tags from MP3 files and correctly tag the Ogg files, as well as
optionally rename them based on those tags.

%prep
%setup -q -n %name

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


