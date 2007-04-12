Summary:	Convert mp3 music files to ogg music files.
Name:		mp32ogg
Version:	0.11
Release:	%mkrel 5
License:	Artistic
Url:		http://faceprint.com/software.phtml
Group:		Sound
Source0:	ftp://ftp.faceprint.com/pub/software/scripts/%{name}-%{version}.bz2
Requires:	perl mpg123 vorbis-tools
BuildRequires:	perl perl-MP3-Info perl-String-ShellQuote
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
# Author: Nathan Walp <faceprint@faceprint.com>

%description
Perl script to convert MP3 files into Ogg Vorbis format. It is able to
read ID3 tags from MP3 files and correctly tag the Ogg files, as well as
optionally rename them based on those tags.

%install
rm -rf %{buildroot}

mkdir -p  %{buildroot}%{_bindir}
bzcat %{SOURCE0} >  %{buildroot}%{_bindir}/%{name}
chmod +x  %{buildroot}%{_bindir}/%{name}
perl -c  %{buildroot}%{_bindir}/%{name}

echo -e "%{name}\n\nAuthor: Nathan Walp <faceprint@faceprint.com>\nLicense: Artistic\n" > README

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*


