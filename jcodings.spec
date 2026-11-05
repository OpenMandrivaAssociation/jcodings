# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jcodings
Version:        1.0.64
Release:        1
Summary:        Java-based codings helper classes for Joni and JRuby


License:        MIT
URL:            https://github.com/jruby/%{name}
Source0:        https://github.com/jruby/jcodings/archive/refs/tags/jcodings-%{version}.tar.gz

BuildArch:      noarch
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name %{name}
%description
Java-based codings helper classes for Joni and JRuby.


%prep
%setup -q -n jcodings-jcodings-%{version}

find -name '*.class' -delete
find -name '*.jar' -delete

%files -f .mfiles
%doc LICENSE.txt README.md
