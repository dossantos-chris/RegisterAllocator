// CS 415, Project 1, block "block9.i"
//
// Fibonacci numbers, using a heap of registers (25)
//
// ** Usage sim -i 1024 0 1 < report3.i

	loadI	1024	=> r0
	loadI	1028	=> r1
	loadI	0	=> r2
	loadI	4	=> r3
	load	r0	=> r2
	load	r1	=> r0

	loadI	2000	=> r1
// f1
loadI 1020 => r4
store r3 => r4
	add	r2, r0	=> r3
// f2
	add	r3, r2	=> r0
// f3
loadI 1016 => r4
store r1 => r4
	add	r0, r3	=> r1
// f4
loadI 1012 => r4
store r3 => r4
	add	r1, r0	=> r3
// f5
loadI 1008 => r4
store r0 => r4
	add	r3, r1	=> r0
// f6
loadI 1004 => r4
store r1 => r4
	add	r0, r3	=> r1
// f7
loadI 1000 => r4
store r3 => r4
	add	r1, r0	=> r3
// f8
loadI 996 => r4
store r0 => r4
	add	r3, r1	=> r0
// f9
loadI 992 => r4
store r1 => r4
	add	r0, r3	=> r1
// f10
loadI 988 => r4
store r3 => r4
	add	r1, r0	=> r3
// 
loadI 984 => r4
store r3 => r4
loadI 1016 => r4
load r4 => r3
	store	r2	=> r3
loadI 1020 => r4
load r4 => r2
loadI 980 => r4
store r1 => r4
	add	r3, r2	=> r1
loadI 1012 => r4
load r4 => r3
	store	r3	=> r1
	add	r1, r2	=> r3
loadI 1008 => r4
load r4 => r1
	store	r1	=> r3
	add	r3, r2	=> r1
loadI 1004 => r4
load r4 => r3
	store	r3	=> r1
	add	r1, r2	=> r3
loadI 1000 => r4
load r4 => r1
	store	r1	=> r3
	add	r3, r2	=> r1
loadI 996 => r4
load r4 => r3
	store	r3	=> r1
	add	r1, r2	=> r3
loadI 992 => r4
load r4 => r1
	store	r1	=> r3
	add	r3, r2	=> r1
loadI 988 => r4
load r4 => r3
	store	r3	=> r1
	add	r1, r2	=> r3
	store	r0	=> r3
	add	r3, r2	=> r0
loadI 980 => r4
load r4 => r1
	store	r1	=> r0
	add	r0, r2	=> r1
loadI 984 => r4
load r4 => r0
	store	r0	=> r1
//
	output	2000
	output	2004
	output	2008
	output	2012
	output	2016
	output	2020
	output	2024
	output	2028
	output	2032
	output	2036
	output	2040
// end of block


