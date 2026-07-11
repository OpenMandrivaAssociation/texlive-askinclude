%global tl_name askinclude
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	Interactive use of \includeonly
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/askinclude
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/askinclude.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package asks the user which files to put in a \includeonly command.
There is provision for answering "same as last time" or "all files".

