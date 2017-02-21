#!/bin/perl

=pod

=head1 NAME

myscript.pl

=head1 SYNOPSIS

myscript.pl <test-case>

=head1 DESCRIPTION

Testee data simulator.

Simulates hard-coded test results for the test of the tool chain itself,
as reference probe for validation of the chain,
and for test of base functions in case of derived classes.

Refer also to the probe simulators in other languages, when debug and step into
the probe itself is required:

=over 3

=item *

myscript.pl - Perl

=item *

myscript.py - Python

=item *

myscript.sh - bash

=item *

ffs.

=back

=head1 OPTIONS

None.

=head1 ARGUMENTS

=cut

###!/usr/bin/env perl
###!/bin/perl

use strict;
use warnings;

my $author  = "Arno-Can Uestuensoez";
my $license = "Artistic-License-2.0 + Forced-Fairplay-Constraints";
my $copyright = "Copyright (C) 2016 Arno-Can Uestuensoez \@Ingenieurbuero Arno-Can Uestuensoez";
my $version = "0.1.14";
my $uuid    = "9de52399-7752-4633-9fdc-66c87a9200b8";

use Sys::Hostname;
use Cwd qw(abs_path), qw(getcwd);
use File::Basename qw(basename), qw(dirname), qw(fileparse);
use lib (
	dirname( dirname( dirname( dirname( dirname abs_path __FILE__ ) ) ) ) );

my $rdbg         = undef;
my $rdbg_default = "localhost:5678";    # the defaults as defined by PyDev

sub printHelpShort {
    print <<"HLP";

SYNOPSIS

   myscript.pl <test-case>

OPTIONS:

  --

ARGUMENTS:

   <test-case> := ( OK | NOK | PRIO | EXITOK | EXITNOK | EXIT7 | EXIT8 | EXIT9OK3NOK2 |STDERRONLY | DEFAULT )

SEE ALSO:

   myscript.pl -help
     More help.

   myscript.pl --help
     POD document.

HLP

   exit(0);

}

sub printHelpPOD {
	system("perldoc", $0);

	exit(0);

}

sub printHelp {
    print <<"HLP";
Provided test cases: ( OK, NOK, PRIO, EXITOK, EXITNOK, EXIT7, EXIT8, EXIT9OK3NOK2, STDERRONLY, DEFAULT )

# A: succeed: OK
  EXIT:
    0
  STDOUT:
    fromA
    arbitrary output
    arbitrary signalling OK string
    arbitrary output
  STDERR:
     --

# B: fail: NOK
  EXIT:
    0
  STDOUT:
    fromB
    arbitrary output
    arbitrary output
  STDERR:
    arbitrary signalling ERROR string

# C: redundancy resolved by user defined priority: PRIO
  EXIT:
    0
  STDOUT:
    fromC
    arbitrary output
    arbitrary signalling OK string
    arbitrary output
  STDERR:
    arbitrary signalling ERROR string

# D: exit value: EXITOK
  EXIT:
    0
  STDOUT:
    fromD
    arbitrary output
    arbitrary signalling OK string
    arbitrary output
  STDERR:
    --

# E: exit value: EXITNOK
  EXIT:
    1
  STDOUT:
    fromE
    arbitrary output
    arbitrary signalling OK string
    arbitrary output
  STDERR:
    --

# F: exit value: EXIT7
  EXIT:
    7
  STDOUT:
    fromF
    arbitrary output
    arbitrary signalling NOK string
    arbitrary output
  STDERR:
    --

# G: exit value: EXIT8
  EXIT:
    8
  STDOUT:
    fromG
    arbitrary output
    arbitrary signalling NOK string
    arbitrary output
  STDERR:
    arbitrary err output
    arbitrary err signalling NOK string
    arbitrary err output

# H: exit value: EXIT9OK3NOK2
  EXIT:
    9
  STDOUT:
    fromH
    OK
    OK
    OK
  STDERR:
    NOK
    NOK

# I: exit value: STDERRONLY
  EXIT:
    0
  STDOUT:
    --
  STDERR:
    fromI
    NOK
    NOK

# DEFAULT: define: here succeed '--default-ok': DEFAULT
  EXIT:
    123
  STDOUT:
    arbitrary output
  STDERR:
    --

HLP

   exit(0);

}


sub call_A_OK {

=pod

=head2 OK

Calls 'call_A_OK'

# A: succeed: OK

  EXIT:

=begin text

        0

=end text

  STDOUT:

=begin text

        fromA
        arbitrary output
        arbitrary signalling OK string
        arbitrary output

=end text

  STDERR:

=begin text

        --

=end text


=cut

	print "fromA\n";
	print "arbitrary output\n";
	print "arbitrary signalling OK string\n";
	print "arbitrary output\n";
	exit(0);
}

sub call_B_NOK {

=pod

=head2 NOK

Calls 'call_B_NOK'

# B: fail: NOK

  EXIT:

=begin text

        0

=end text

  STDOUT:

=begin text

        fromB
        arbitrary output
        arbitrary output

=end text

  STDERR:

=begin text

        arbitrary signalling ERROR string

=end text

=cut

	print "fromB\n";
	print "arbitrary output\n";
	print STDERR "arbitrary signalling ERROR string\n";
	print "arbitrary output\n";
	exit(0);
}

sub call_C_PRIO {

=pod

=head2 PRIO

Calls 'call_C_PRIO'

# C: redundancy resolved by user defined priority: PRIO

  EXIT:

=begin text

        0

=end text

  STDOUT:

=begin text

        fromC
        arbitrary output
        arbitrary signalling OK string
        arbitrary output

=end text

  STDERR:

=begin text

        arbitrary signalling ERROR string

=end text

=cut

	print "fromC\n";
	print "arbitrary output\n";
	print "arbitrary signalling OK string\n";
	print "arbitrary output\n";
	print STDERR "arbitrary signalling ERROR string\n";
	exit(0);
}

sub call_D_EXITOK {

=pod

=head2 EXITOK

Calls: 'call_D_EXITOK'

# D: exit value: EXITOK

  EXIT:

=begin text

        0

=end text

  STDOUT:

=begin text

        fromD
        arbitrary output
        arbitrary signalling OK string
        arbitrary output

=end text

  STDERR:

=begin text

        --

=end text

=cut

	print "fromD\n";
	print "arbitrary output\n";
	print "arbitrary signalling OK string\n";
	print "arbitrary output\n";
	exit(0);
}

sub call_E_EXITNOK {

=pod

=head2 EXITNOK

Call 'call_D_EXITNOK'

# E: exit value: EXITNOK

  EXIT:

=begin text

        1

=end text

  STDOUT:

=begin text

        fromE
        arbitrary output
        arbitrary signalling OK string
        arbitrary output

=end text

  STDERR:

=begin text

        --

=end text

=cut

	print "fromE\n";
	print "arbitrary output\n";
	print "arbitrary signalling OK string\n";
	print "arbitrary output\n";
	exit(1);
}

sub call_F_EXIT7 {

=pod

=head2 EXIT7

Calls 'call_F_EXIT7'

# F: exit value: EXIT7

  EXIT:

=begin text

        7

=end text

  STDOUT:

=begin text

        fromF
        arbitrary output
        arbitrary signalling NOK string
        arbitrary output

=end text

  STDERR:

=begin text

        --

=end text

=cut

	print "fromF\n";
	print "arbitrary output\n";
	print "arbitrary signalling NOK string\n";
	print "arbitrary output\n";
	exit(7);
}

sub call_G_EXIT8 {

=pod

=head2 EXIT8

Calls 'call_G_EXIT8'

# G: exit value: EXIT8

  EXIT:

=begin text

        8

=end text

  STDOUT:

=begin text

        from G
        arbitrary output
        arbitrary signalling NOK string
        arbitrary output

=end text

  STDERR:

=begin text

        arbitrary err output
        arbitrary err signalling NOK string
        arbitrary err output

=end text

=cut

	print "fromG\n";
	print "arbitrary output\n";
	print "arbitrary signalling NOK string\n";
	print "arbitrary output\n";
	print STDERR "arbitrary err output\n";
	print STDERR "arbitrary err signalling NOK string\n";
	print STDERR "arbitrary err output\n";
	exit(8);
}

sub call_H_EXIT9OK3NOK2 {

=pod

=head2 EXIT9OK3NOK2

Calls 'call_H_EXIT9OK3NOK2'

# H: exit value: EXIT9OK3NOK2

  EXIT:

=begin text

        9

=end text

  STDOUT:

=begin text

        fromH
        OK
        OK
        OK

=end text

  STDERR:

=begin text

        NOK
        NOK

=end text

=cut

	print "fromH\n";
	print "OK\n";
	print "OK\n";
	print "OK\n";
	print STDERR "NOK\n";
	print STDERR "NOK\n";
	exit(9);
}

sub call_I_STDERRONLY {

=pod

=head2 STDERRONLY

Calls 'call_I_STDERRONLY'

# I: exit value: STDERRONLY

  EXIT:

=begin text

        0

=end text

  STDOUT:

=begin text

        --

=end text

  STDERR:

=begin text

        fromI
        NOK
        NOK

=end text

=cut

	print STDERR "fromI\n";
	print STDERR "NOK\n";
	print STDERR "NOK\n";
	exit(0);
}

sub call_DEFAULT {

=pod

=head2 DEFAULT

Calls 'DEFAULT'

# DEFAULT: define: here succeed '--default-ok': DEFAULT

  EXIT:

=begin text

        123

=end text

  STDOUT:

=begin text

        arbitrary output

=end text

  STDERR:

=begin text

        --

=end text

=cut

	print "arbitrary output\n";
	exit(123);
}


my $argnum = 0;
my $num_args = $#ARGV + 1;

foreach $argnum (0 .. $#ARGV) {
    if ($ARGV[$argnum] =~ "--rdbg"){
		;

		#
		#TODO: port to Perl
		#
	}
}


my $ax;
foreach $argnum (0 .. $#ARGV) {
	$ax = $ARGV[$argnum];
	$ax = uc $ax;
    if ($ax =~ /--HELP/){
    	printHelpPOD($ARGV[0]);
    }
    elsif ($ax =~ /-HELP/){
    	printHelp();
    }
    elsif ($ax =~ /-H/ ){
    	printHelpShort();
    }
    elsif ($ax =~ '^OK$'){
        call_A_OK();
        exit(0);
    }
    elsif ($ax =~ '^NOK$'){
        call_B_NOK();
        exit(0);
    }
    elsif ($ax =~ '^PRIO$'){
        call_C_PRIO();
        exit(0);
    }
    elsif ($ax =~ '^EXITOK$'){
        call_D_EXITOK();
        exit(0);
    }
    elsif ($ax =~ '^EXITNOK$'){
        call_E_EXITNOK();
        exit(1);
    }
    elsif ($ax =~ '^EXIT7$'){
        call_F_EXIT7();
        exit(7);
    }
    elsif ($ax =~ '^EXIT8$'){
        call_G_EXIT8();
        exit(8);
    }
    elsif ($ax =~ '^EXIT9OK3NOK2$'){
        call_H_EXIT9OK3NOK2();
        exit(9);
    }
    elsif ($ax =~ '^STDERRONLY$'){
        call_I_STDERRONLY();
        exit(0);
    }
    elsif ($ax =~ '^--$'){
        my $x=1;
    }
    else{
        call_DEFAULT();
        exit(123);
    }
}

# DEFAULT: define: here succeed '--default-ok'
call_DEFAULT();
exit(123);

__END__
=head1 SEE ALSO

L<http://pypi.python.org/pypi/epyunit>

L<http://epyunit.sourceforge.net>

=head1 COPYRIGHT

Copyright (C) 2016 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

=head1 LICENSE

Artistic-License-2.0 + Forced-Fairplay-Constraints


=cut



