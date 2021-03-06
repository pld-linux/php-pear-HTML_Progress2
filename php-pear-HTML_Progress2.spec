%define		_status		stable
%define		_pearname	HTML_Progress2
Summary:	%{_pearname} - include a loading bar in your XHTML documents quickly and easily
Summary(pl.UTF-8):	%{_pearname} - dołączanie paska postępu w dokumentach XHTML w szybki i prosty sposób
Name:		php-pear-%{_pearname}
Version:	2.4.2
Release:	2
License:	PHP License 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	da422b743c9cdbf38e1d55cd3d64e18f
URL:		http://pear.php.net/package/HTML_Progress2/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.2.0
Requires:	php-pear
Requires:	php-pear-Event_Dispatcher >= 0.9.1
Requires:	php-pear-HTML_CSS >= 1.1.2
Requires:	php-pear-HTML_Common >= 1.2.1
Requires:	php-pear-PEAR-core >= 1:1.4.3
Requires:	php-pear-PHP_Compat >= 1.4.1
Suggests:	php-gd
Suggests:	php-pear-HTML_AJAX
Suggests:	php-pear-HTML_Page2
Suggests:	php-pear-HTML_QuickForm
Suggests:	php-pear-HTML_QuickForm_Controller
Suggests:	php-pear-HTML_QuickForm_Renderer_Tableless
Suggests:	php-pear-HTML_Template_IT
Suggests:	php-pear-HTML_Template_Sigma
Suggests:	php-pear-Image_Color
Suggests:	php-pear-Log
Suggests:	php-pear-PHP_Compat
Obsoletes:	php-pear-HTML_Progress2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PEAR.*)' 'pear(HTML/QuickForm.*)' 'pear(HTML/QuickForm/Controller.*)' 'pear(Image/Color.*)' 'pear(HTML/Page2.*)' 'pear(HTML/Template/IT.*)' 'pear(HTML/Template/Sigma.*)' 'pear(Log.*)' 'pear(gd.*)' 'pear(Smarty.*)' 'pear(PHP/Compat.*)' 'pear(HTML/QuickForm/Renderer/Tableless.*)' pear(HTML/AJAX.*)

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

%description -l pl.UTF-8
Ten pakiet dostarcza sposób na dodanie w istniejących dokumentach
XHTML w pełni konfigurowalnego paska postępu. Przeglądarka musi
obsługiwać DHTML.

Możliwości:
- tworzenie poziomego lub pionowego paska, a także okręgu, elipsy i
  wielokątów (kwadratu, prostokąta)
- umożliwia zastosowanie istniejących zewnętrznych arkuszy styli i/lub
  JavaScriptu
- wszystkie elementy (postęp, komórki, etykiety) są konfigurowalne
  poprzez ich właściwości HTML
- procenty/etykiety są umieszczone naokoło miernika postępu
- jest zgodny ze wszystkimi standardami CSS/XHTML
- bardzo łatwa integracja ze wszystkimi silnikami szablonów
- implementuje wzorzec projektowy Observer; można dodać Listeners
- dodaje konfigurowalny wzorzec monitora do wyświetlania paska
  postępu; użytkownik końcowy może przerwać postęp w dowolnej chwili
- pozwala na istnienie wielu mierników postępu na tej samej stronie
  bez użycia iframe
 - system obsługi błędów obsługujący natywny PEAR_Error, ale także
   PEAR_ErrorStack, a także dowolny inny system, który chcemy podłączyć
- gotowy na PHP 5.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/data/HTML_Progress2/
%{php_pear_dir}/HTML/Progress2
%{php_pear_dir}/HTML/Progress2.php
%{php_pear_dir}/HTML/Progress2_Lite.php
