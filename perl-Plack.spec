#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : perl-Plack
Version  : 1.0051
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-1.0051.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Plack-1.0051.tar.gz
Summary  : 'Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Plack-bin = %{version}-%{release}
Requires: perl-Plack-license = %{version}-%{release}
Requires: perl-Plack-man = %{version}-%{release}
Requires: perl-Plack-perl = %{version}-%{release}
Requires: perl(Apache2::RequestRec)
Requires: perl(Apache::LogFormat::Compiler)
Requires: perl(CGI::Emulate::PSGI)
Requires: perl(Cookie::Baker)
Requires: perl(Devel::StackTrace)
Requires: perl(Devel::StackTrace::AsHTML)
Requires: perl(File::ShareDir)
Requires: perl(File::pushd)
Requires: perl(HTTP::Date)
Requires: perl(HTTP::Entity::Parser)
Requires: perl(HTTP::Headers)
Requires: perl(HTTP::Headers::Fast)
Requires: perl(HTTP::MultiPartParser)
Requires: perl(HTTP::Request)
Requires: perl(HTTP::Response)
Requires: perl(HTTP::Status)
Requires: perl(Hash::MultiValue)
Requires: perl(JSON::MaybeXS)
Requires: perl(Module::Refresh)
Requires: perl(POSIX::strftime::Compiler)
Requires: perl(Stream::Buffered)
Requires: perl(URI::Escape)
Requires: perl(WWW::Form::UrlEncoded)
BuildRequires : buildreq-cpan
BuildRequires : perl(Apache::LogFormat::Compiler)
BuildRequires : perl(Cookie::Baker)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Devel::StackTrace::AsHTML)
BuildRequires : perl(Digest::MD5)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Filesys::Notify::Simple)
BuildRequires : perl(HTTP::Date)
BuildRequires : perl(HTTP::Entity::Parser)
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(HTTP::Headers::Fast)
BuildRequires : perl(HTTP::Message)
BuildRequires : perl(HTTP::MultiPartParser)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(HTTP::Status)
BuildRequires : perl(Hash::MultiValue)
BuildRequires : perl(JSON::MaybeXS)
BuildRequires : perl(LWP::MediaTypes)
BuildRequires : perl(POSIX::strftime::Compiler)
BuildRequires : perl(Stream::Buffered)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Test::SharedFork)
BuildRequires : perl(Test::TCP)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(URI)
BuildRequires : perl(URI::Escape)
BuildRequires : perl(WWW::Form::UrlEncoded)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Plack - Perl Superglue for Web frameworks and Web Servers (PSGI
toolkit)
DESCRIPTION

%package bin
Summary: bin components for the perl-Plack package.
Group: Binaries
Requires: perl-Plack-license = %{version}-%{release}

%description bin
bin components for the perl-Plack package.


%package dev
Summary: dev components for the perl-Plack package.
Group: Development
Requires: perl-Plack-bin = %{version}-%{release}
Provides: perl-Plack-devel = %{version}-%{release}
Requires: perl-Plack = %{version}-%{release}

%description dev
dev components for the perl-Plack package.


%package license
Summary: license components for the perl-Plack package.
Group: Default

%description license
license components for the perl-Plack package.


%package man
Summary: man components for the perl-Plack package.
Group: Default

%description man
man components for the perl-Plack package.


%package perl
Summary: perl components for the perl-Plack package.
Group: Default
Requires: perl-Plack = %{version}-%{release}

%description perl
perl components for the perl-Plack package.


%prep
%setup -q -n Plack-1.0051
cd %{_builddir}/Plack-1.0051
pushd ..
cp -a Plack-1.0051 buildavx2
popd
pushd ..
cp -a Plack-1.0051 buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Plack
cp %{_builddir}/Plack-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Plack/0e926b5f665579b161e070ef2a96c8c57c919673 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/plackup

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Message::PSGI.3
/usr/share/man/man3/HTTP::Server::PSGI.3
/usr/share/man/man3/Plack.3
/usr/share/man/man3/Plack::App::CGIBin.3
/usr/share/man/man3/Plack::App::Cascade.3
/usr/share/man/man3/Plack::App::Directory.3
/usr/share/man/man3/Plack::App::File.3
/usr/share/man/man3/Plack::App::PSGIBin.3
/usr/share/man/man3/Plack::App::URLMap.3
/usr/share/man/man3/Plack::App::WrapCGI.3
/usr/share/man/man3/Plack::Builder.3
/usr/share/man/man3/Plack::Component.3
/usr/share/man/man3/Plack::HTTPParser.3
/usr/share/man/man3/Plack::HTTPParser::PP.3
/usr/share/man/man3/Plack::Handler.3
/usr/share/man/man3/Plack::Handler::Apache1.3
/usr/share/man/man3/Plack::Handler::Apache2.3
/usr/share/man/man3/Plack::Handler::Apache2::Registry.3
/usr/share/man/man3/Plack::Handler::CGI.3
/usr/share/man/man3/Plack::Handler::FCGI.3
/usr/share/man/man3/Plack::Handler::HTTP::Server::PSGI.3
/usr/share/man/man3/Plack::Handler::Standalone.3
/usr/share/man/man3/Plack::LWPish.3
/usr/share/man/man3/Plack::Loader.3
/usr/share/man/man3/Plack::Loader::Delayed.3
/usr/share/man/man3/Plack::Loader::Restarter.3
/usr/share/man/man3/Plack::Loader::Shotgun.3
/usr/share/man/man3/Plack::MIME.3
/usr/share/man/man3/Plack::Middleware.3
/usr/share/man/man3/Plack::Middleware::AccessLog.3
/usr/share/man/man3/Plack::Middleware::AccessLog::Timed.3
/usr/share/man/man3/Plack::Middleware::Auth::Basic.3
/usr/share/man/man3/Plack::Middleware::BufferedStreaming.3
/usr/share/man/man3/Plack::Middleware::Chunked.3
/usr/share/man/man3/Plack::Middleware::Conditional.3
/usr/share/man/man3/Plack::Middleware::ConditionalGET.3
/usr/share/man/man3/Plack::Middleware::ContentLength.3
/usr/share/man/man3/Plack::Middleware::ContentMD5.3
/usr/share/man/man3/Plack::Middleware::ErrorDocument.3
/usr/share/man/man3/Plack::Middleware::HTTPExceptions.3
/usr/share/man/man3/Plack::Middleware::Head.3
/usr/share/man/man3/Plack::Middleware::IIS6ScriptNameFix.3
/usr/share/man/man3/Plack::Middleware::IIS7KeepAliveFix.3
/usr/share/man/man3/Plack::Middleware::JSONP.3
/usr/share/man/man3/Plack::Middleware::LighttpdScriptNameFix.3
/usr/share/man/man3/Plack::Middleware::Lint.3
/usr/share/man/man3/Plack::Middleware::Log4perl.3
/usr/share/man/man3/Plack::Middleware::LogDispatch.3
/usr/share/man/man3/Plack::Middleware::NullLogger.3
/usr/share/man/man3/Plack::Middleware::RearrangeHeaders.3
/usr/share/man/man3/Plack::Middleware::Recursive.3
/usr/share/man/man3/Plack::Middleware::Refresh.3
/usr/share/man/man3/Plack::Middleware::Runtime.3
/usr/share/man/man3/Plack::Middleware::SimpleContentFilter.3
/usr/share/man/man3/Plack::Middleware::SimpleLogger.3
/usr/share/man/man3/Plack::Middleware::StackTrace.3
/usr/share/man/man3/Plack::Middleware::Static.3
/usr/share/man/man3/Plack::Middleware::XFramework.3
/usr/share/man/man3/Plack::Middleware::XSendfile.3
/usr/share/man/man3/Plack::Request.3
/usr/share/man/man3/Plack::Request::Upload.3
/usr/share/man/man3/Plack::Response.3
/usr/share/man/man3/Plack::Runner.3
/usr/share/man/man3/Plack::Test.3
/usr/share/man/man3/Plack::Test::MockHTTP.3
/usr/share/man/man3/Plack::Test::Server.3
/usr/share/man/man3/Plack::Test::Suite.3
/usr/share/man/man3/Plack::Util.3
/usr/share/man/man3/Plack::Util::Accessor.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Plack/0e926b5f665579b161e070ef2a96c8c57c919673

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/plackup.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
