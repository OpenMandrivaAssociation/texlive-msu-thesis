Name:		texlive-msu-thesis
Version:	65282
Release:	1
Summary:	Class for Michigan State University Master's and PhD theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/msu-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a class file for producing dissertations and theses
according to the Michigan State University Graduate School
Guidelines for Electronic Submission of Master's Theses and
Dissertations (2010). The class is based on the memoir document
class, and thefore inherits all of the functionality of that
class.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/msu-thesis
%doc %{_texmfdistdir}/doc/latex/msu-thesis

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
