%define	oname	plist

Summary:	A ruby library to manipulate Property List files
Name:		rubygem-%{oname}
Version:	3.0.0
Release:	%mkrel 2
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Plist is a library to manipulate Property List files, also known as plists.
It can parse plist files into native Ruby data structures as well as generating
new plist files from your Ruby objects.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/ext

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.0-2mdv2011.0
+ Revision: 614776
- the mass rebuild of 2010.1 packages

* Wed Feb 03 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.0.0-1mdv2010.1
+ Revision: 500471
- drop bogus dependencies
- import rubygem-plist


* Mon Feb  3 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.0.0-1
- initial release
