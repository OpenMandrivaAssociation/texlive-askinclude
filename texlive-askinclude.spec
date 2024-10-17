Name:		texlive-askinclude
Version:	54725
Release:	2
Summary:	Interactive use of \includeonly
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/askinclude
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package asks the user which files to put in a \includeonly
command. There is provision for answering "same as last time"
or "all files".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/askinclude
%{_texmfdistdir}/tex/latex/askinclude
%doc %{_texmfdistdir}/doc/latex/askinclude

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
