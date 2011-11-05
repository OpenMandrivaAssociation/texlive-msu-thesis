# revision 24055
# category Package
# catalog-ctan /macros/latex/contrib/msu-thesis
# catalog-date 2011-09-21 01:15:36 +0200
# catalog-license lppl1.3
# catalog-version 2.1
Name:		texlive-msu-thesis
Version:	2.1
Release:	1
Summary:	Class for Michigan State University Master's and PhD theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/msu-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/msu-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a class file for producing dissertations and theses
according to the Michigan State University Graduate School
Guidelines for Electronic Submission of Master's Theses and
Dissertations (2010). The class is based on the memoir document
class, and thefore inherits all of the functionality of that
class.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/msu-thesis/gb4e-compat.tex
%{_texmfdistdir}/tex/latex/msu-thesis/msu-thesis.cls
%doc %{_texmfdistdir}/doc/latex/msu-thesis/README
%doc %{_texmfdistdir}/doc/latex/msu-thesis/msu-thesis.pdf
%doc %{_texmfdistdir}/doc/msu-thesis/msu-thesis.tex
%doc %{_texmfdistdir}/doc/msu-thesis/samples/MSU-thesis-template.pdf
%doc %{_texmfdistdir}/doc/msu-thesis/samples/MSU-thesis-template.tex
%doc %{_texmfdistdir}/doc/msu-thesis/samples/MSU-thesis-testfile.bib
%doc %{_texmfdistdir}/doc/msu-thesis/samples/MSU-thesis-testfile.pdf
%doc %{_texmfdistdir}/doc/msu-thesis/samples/MSU-thesis-testfile.tex
%doc %{_texmfdistdir}/doc/msu-thesis/samples/unified.bst
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
