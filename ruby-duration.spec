Summary:	A library to manage durations of time
Name:		ruby-duration
Version:	0.1.0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/duration-%{version}.gem
# Source0-md5:	33b5ba848609f209dd46e82cced6b151
#Patch0: %{name}-nogems.patch
URL:		http://rubyforge.org/projects/duration
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
#%patch0 -p1
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/duration.rb
%{ruby_rubylibdir}/duration/holidays.rb
%{ruby_rubylibdir}/duration/locale.rb
%{ruby_rubylibdir}/duration/localizations.rb
%{ruby_rubylibdir}/duration/localizations/english.rb
%{ruby_rubylibdir}/duration/localizations/korean.rb
%{ruby_rubylibdir}/duration/numeric.rb
%{ruby_rubylibdir}/duration/time.rb
%{ruby_rubylibdir}/duration/version.rb
