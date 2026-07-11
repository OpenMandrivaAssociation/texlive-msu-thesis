%global tl_name msu-thesis
%global tl_revision 71883

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3b
Release:	%{tl_revision}.1
Summary:	Class for Michigan State University Masters and PhD theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/msu-thesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a class file for producing dissertations and theses according to
the Michigan State University Graduate School Guidelines for Electronic
Submission of Master's Theses and Dissertations. The class should meet
all current requirements and is updated whenever the university
guidelines change. The class is based on the memoir document class, and
inherits the functionality of that class.

