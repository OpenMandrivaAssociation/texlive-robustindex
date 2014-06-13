# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/robustindex
# catalog-date 2007-02-26 15:09:49 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-robustindex
Version:	20070226
Release:	7
Summary:	Create index with pagerefs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/robustindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/robustindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Third parties often change the page numbers without rerunning
makeindex. One would like to make the page numbers in the index
entries more robust. This bundle provides robustindex.sty and
robustglossary.sty, which use the \pageref mechanism to
maintain correct page numbers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/robustindex/robustglossary.sty
%{_texmfdistdir}/tex/latex/robustindex/robustindex.sty
%doc %{_texmfdistdir}/doc/latex/robustindex/README
%doc %{_texmfdistdir}/doc/latex/robustindex/robustindex.html
%doc %{_texmfdistdir}/doc/latex/robustindex/robustsample.pdf
%doc %{_texmfdistdir}/doc/latex/robustindex/robustsample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070226-2
+ Revision: 755719
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070226-1
+ Revision: 719458
- texlive-robustindex
- texlive-robustindex
- texlive-robustindex
- texlive-robustindex

