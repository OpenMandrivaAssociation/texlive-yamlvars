Name:		texlive-yamlvars
Version:	72052
Release:	1
Summary:	A YAML parser and tool for easy LaTeX definition creation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yamlvars
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yamlvars.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yamlvars.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LuaLaTeX package provides a YAML parser and some functions
to declare and define LaTeX definitions using YAML files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/yamlvars
%doc %{_texmfdistdir}/doc/lualatex/yamlvars

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
