Name:		texlive-robustindex
Version:	20171003
Release:	1
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
%{_texmfdistdir}/tex/latex/robustindex
%doc %{_texmfdistdir}/doc/latex/robustindex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
