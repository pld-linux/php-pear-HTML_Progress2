%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Progress2
%define		_status		stable
%define		_pearname	HTML_Progress2

Summary:	%{_pearname} - include a loading bar in your XHTML documents quickly and easily
Summary(pl):	%{_pearname} - do³±czanie paska postêpu w dokumentach XHTML w szybki i prosty sposób
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	1
Epoch:		0
License:	PHP License 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d904a0d117d810b1c9f2eef8a7d7cca0
URL:		http://pear.php.net/package/HTML_Progress2/
Requires:	php-pear
Requires:	php-common >= 3:4.2.0
Requires:	php-pear-PHP_Compat >= 1.4.1
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	php-pear-Event_Dispatcher >= 0.9.1
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PEAR.*)' 'pear(HTML/QuickForm.*)' 'pear(HTML/QuickForm/Controller.*)' 'pear(Image/Color.*)' 'pear(HTML/Page2.*)' 'pear(HTML/Template/IT.*)' 'pear(HTML/Template/Sigma.*)' 'pear(Log.*)' 'pear(gd.*)' 'pear(Smarty.*)'

%description
This package provides a way to add a loading bar fully customizable in
existing XHTML documents. Your browser should accept DHTML feature.

Features:
- create horizontal, vertival bar and also circle, ellipse and
  polygons (square, rectangle).
- allows usage of existing external StyleSheet and/or JavaScript.
- all elements (progress, cells, labels) are customizable by their
  HTML properties.
- percent/labels are floating all around the progress meter.
- compliant with all CSS/XHMTL standards.
- integration with all template engines is very easy.
- implements Observer design pattern. It is possible to add Listeners.
- adds a customizable monitor pattern to display a progress bar.
  User-end can abort progress at any time.
- allows many progress meter on same page without uses of iframe
  solution.
- error handling system that support native PEAR_Error, but also
  PEAR_ErrorStack, and any other system you might want to plug-in.
- PHP 5 ready.

In PEAR status of this package is: %{_status}.

%description -l pl 
Ten pakiet dostarcza sposób na dodanie w istniej±cych dokumentach
XHTML w pe³ni konfigurowalnego paska postêpu. Przegl±darka musi
obs³ugiwaæ DHTML.

Mo¿liwo¶ci:
- tworzenie poziomego lub pionowego paska, a tak¿e okrêgu, elipsy i
  wielok±tów (kwadratu, prostok±ta)
- umo¿liwia zastosowanie istniej±cych zewnêtrznych arkuszy styli i/lub
  JavaScriptu
- wszystkie elementy (postêp, komórki, etykiety) s± konfigurowalne
  poprzez ich w³a¶ciwo¶ci HTML
- procenty/etykiety s± umieszczone naoko³o miernika postêpu
- jest zgodny ze wszystkimi standardami CSS/XHTML
- bardzo ³atwa integracja ze wszystkimi silnikami szablonów
- implementuje wzorzec projektowy Observer; mo¿na dodaæ Listeners
- dodaje konfigurowalny wzorzec monitora do wy¶wietlania paska
  postêpu; u¿ytkownik koñcowy mo¿e przerwaæ postêp w dowolnej chwili
- pozwala na istnienie wielu mierników postêpu na tej samej stronie
  bez u¿ycia iframe
 - system obs³ugi b³êdów obs³uguj±cy natywny PEAR_Error, ale tak¿e
  PEAR_ErrorStack, a tak¿e dowolny inny system, który chcemy pod³±czyæ
- gotowy na PHP 5.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt docs
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/Progress2
%{php_pear_dir}/HTML/Progress2.php
%{php_pear_dir}/HTML/Progress2_Lite.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/HTML_Progress2
