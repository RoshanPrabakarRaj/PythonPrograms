Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a="loop"
>>> def foo():
	print("another loop")
	while a == "loop";
	//print
SyntaxError: invalid syntax
>>> a="loop"
>>> def foo():
	print("another loop")
	while a == "loop":
		
SyntaxError: multiple statements found while compiling a single statement
>>> a="loop"
>>> def foo():
	print("another")
	while a == "loop":
		foo()

		
>>> y="234"
>>> y
'234'
>>> print y
SyntaxError: Missing parentheses in call to 'print'
>>> print(y)
234
>>> a="roshan 'what' are you doing?"
>>> print (a)
roshan 'what' are you doing?
>>> fake = """
what are you doing?
doing some python coding..
"""
>>> print (fake)

what are you doing?
doing some python coding..

>>> hi="what\"n are you doing?
SyntaxError: EOL while scanning string literal
>>> hi="what\"n are you doing?"
>>> print (hi)
what"n are you doing?
>>> cheese = "cheese available:\n parmesan \n garlic"
>>> print (cheese)
cheese available:
 parmesan 
 garlic
>>> x=("hello"
   "world")
>>> print (x)
helloworld
>>> x="hello"
>>> y=("helloe"
   "\tworld")
>>> print (y)
helloe	world
>>> python fibonacci.py
SyntaxError: invalid syntax
>>> Python fibonacci.py
SyntaxError: invalid syntax
>>> Python fibonacci.py
SyntaxError: invalid syntax
>>> a=0
>>> b=1
>>> while b < 150 :
	print(b)
	a=b
	b=a+b

	
1
2
4
8
16
32
64
128
>>>  python -i fibonacci.py
 
SyntaxError: unexpected indent
>>> python -i fibonacci.py
SyntaxError: invalid syntax
>>> debug
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    debug
NameError: name 'debug' is not defined
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/fibonacci.py 
1
1
2
3
5
8
13
21
34
55
89
144
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/primeNumber.py 
2 is a prime number
3 is a prime number
4 equals 2 * 2.0
5 is a prime number
6 equals 2 * 3.0
7 is a prime number
8 equals 2 * 4.0
9 equals 3 * 3.0
10 equals 2 * 5.0
11 is a prime number
12 equals 2 * 6.0
13 is a prime number
14 equals 2 * 7.0
15 equals 3 * 5.0
16 equals 2 * 8.0
17 is a prime number
18 equals 2 * 9.0
19 is a prime number
20 equals 2 * 10.0
21 equals 3 * 7.0
22 equals 2 * 11.0
23 is a prime number
24 equals 2 * 12.0
25 equals 5 * 5.0
26 equals 2 * 13.0
27 equals 3 * 9.0
28 equals 2 * 14.0
29 is a prime number
30 equals 2 * 15.0
31 is a prime number
32 equals 2 * 16.0
33 equals 3 * 11.0
34 equals 2 * 17.0
35 equals 5 * 7.0
36 equals 2 * 18.0
37 is a prime number
38 equals 2 * 19.0
39 equals 3 * 13.0
40 equals 2 * 20.0
41 is a prime number
42 equals 2 * 21.0
43 is a prime number
44 equals 2 * 22.0
45 equals 3 * 15.0
46 equals 2 * 23.0
47 is a prime number
48 equals 2 * 24.0
49 equals 7 * 7.0
50 equals 2 * 25.0
51 equals 3 * 17.0
52 equals 2 * 26.0
53 is a prime number
54 equals 2 * 27.0
55 equals 5 * 11.0
56 equals 2 * 28.0
57 equals 3 * 19.0
58 equals 2 * 29.0
59 is a prime number
60 equals 2 * 30.0
61 is a prime number
62 equals 2 * 31.0
63 equals 3 * 21.0
64 equals 2 * 32.0
65 equals 5 * 13.0
66 equals 2 * 33.0
67 is a prime number
68 equals 2 * 34.0
69 equals 3 * 23.0
70 equals 2 * 35.0
71 is a prime number
72 equals 2 * 36.0
73 is a prime number
74 equals 2 * 37.0
75 equals 3 * 25.0
76 equals 2 * 38.0
77 equals 7 * 11.0
78 equals 2 * 39.0
79 is a prime number
80 equals 2 * 40.0
81 equals 3 * 27.0
82 equals 2 * 41.0
83 is a prime number
84 equals 2 * 42.0
85 equals 5 * 17.0
86 equals 2 * 43.0
87 equals 3 * 29.0
88 equals 2 * 44.0
89 is a prime number
90 equals 2 * 45.0
91 equals 7 * 13.0
92 equals 2 * 46.0
93 equals 3 * 31.0
94 equals 2 * 47.0
95 equals 5 * 19.0
96 equals 2 * 48.0
97 is a prime number
98 equals 2 * 49.0
99 equals 3 * 33.0
100 equals 2 * 50.0
101 is a prime number
102 equals 2 * 51.0
103 is a prime number
104 equals 2 * 52.0
105 equals 3 * 35.0
106 equals 2 * 53.0
107 is a prime number
108 equals 2 * 54.0
109 is a prime number
110 equals 2 * 55.0
111 equals 3 * 37.0
112 equals 2 * 56.0
113 is a prime number
114 equals 2 * 57.0
115 equals 5 * 23.0
116 equals 2 * 58.0
117 equals 3 * 39.0
118 equals 2 * 59.0
119 equals 7 * 17.0
120 equals 2 * 60.0
121 equals 11 * 11.0
122 equals 2 * 61.0
123 equals 3 * 41.0
124 equals 2 * 62.0
125 equals 5 * 25.0
126 equals 2 * 63.0
127 is a prime number
128 equals 2 * 64.0
129 equals 3 * 43.0
130 equals 2 * 65.0
131 is a prime number
132 equals 2 * 66.0
133 equals 7 * 19.0
134 equals 2 * 67.0
135 equals 3 * 45.0
136 equals 2 * 68.0
137 is a prime number
138 equals 2 * 69.0
139 is a prime number
140 equals 2 * 70.0
141 equals 3 * 47.0
142 equals 2 * 71.0
143 equals 11 * 13.0
144 equals 2 * 72.0
145 equals 5 * 29.0
146 equals 2 * 73.0
147 equals 3 * 49.0
148 equals 2 * 74.0
149 is a prime number
150 equals 2 * 75.0
151 is a prime number
152 equals 2 * 76.0
153 equals 3 * 51.0
154 equals 2 * 77.0
155 equals 5 * 31.0
156 equals 2 * 78.0
157 is a prime number
158 equals 2 * 79.0
159 equals 3 * 53.0
160 equals 2 * 80.0
161 equals 7 * 23.0
162 equals 2 * 81.0
163 is a prime number
164 equals 2 * 82.0
165 equals 3 * 55.0
166 equals 2 * 83.0
167 is a prime number
168 equals 2 * 84.0
169 equals 13 * 13.0
170 equals 2 * 85.0
171 equals 3 * 57.0
172 equals 2 * 86.0
173 is a prime number
174 equals 2 * 87.0
175 equals 5 * 35.0
176 equals 2 * 88.0
177 equals 3 * 59.0
178 equals 2 * 89.0
179 is a prime number
180 equals 2 * 90.0
181 is a prime number
182 equals 2 * 91.0
183 equals 3 * 61.0
184 equals 2 * 92.0
185 equals 5 * 37.0
186 equals 2 * 93.0
187 equals 11 * 17.0
188 equals 2 * 94.0
189 equals 3 * 63.0
190 equals 2 * 95.0
191 is a prime number
192 equals 2 * 96.0
193 is a prime number
194 equals 2 * 97.0
195 equals 3 * 65.0
196 equals 2 * 98.0
197 is a prime number
198 equals 2 * 99.0
199 is a prime number
200 equals 2 * 100.0
201 equals 3 * 67.0
202 equals 2 * 101.0
203 equals 7 * 29.0
204 equals 2 * 102.0
205 equals 5 * 41.0
206 equals 2 * 103.0
207 equals 3 * 69.0
208 equals 2 * 104.0
209 equals 11 * 19.0
210 equals 2 * 105.0
211 is a prime number
212 equals 2 * 106.0
213 equals 3 * 71.0
214 equals 2 * 107.0
215 equals 5 * 43.0
216 equals 2 * 108.0
217 equals 7 * 31.0
218 equals 2 * 109.0
219 equals 3 * 73.0
220 equals 2 * 110.0
221 equals 13 * 17.0
222 equals 2 * 111.0
223 is a prime number
224 equals 2 * 112.0
225 equals 3 * 75.0
226 equals 2 * 113.0
227 is a prime number
228 equals 2 * 114.0
229 is a prime number
230 equals 2 * 115.0
231 equals 3 * 77.0
232 equals 2 * 116.0
233 is a prime number
234 equals 2 * 117.0
235 equals 5 * 47.0
236 equals 2 * 118.0
237 equals 3 * 79.0
238 equals 2 * 119.0
239 is a prime number
240 equals 2 * 120.0
241 is a prime number
242 equals 2 * 121.0
243 equals 3 * 81.0
244 equals 2 * 122.0
245 equals 5 * 49.0
246 equals 2 * 123.0
247 equals 13 * 19.0
248 equals 2 * 124.0
249 equals 3 * 83.0
250 equals 2 * 125.0
251 is a prime number
252 equals 2 * 126.0
253 equals 11 * 23.0
254 equals 2 * 127.0
255 equals 3 * 85.0
256 equals 2 * 128.0
257 is a prime number
258 equals 2 * 129.0
259 equals 7 * 37.0
260 equals 2 * 130.0
261 equals 3 * 87.0
262 equals 2 * 131.0
263 is a prime number
264 equals 2 * 132.0
265 equals 5 * 53.0
266 equals 2 * 133.0
267 equals 3 * 89.0
268 equals 2 * 134.0
269 is a prime number
270 equals 2 * 135.0
271 is a prime number
272 equals 2 * 136.0
273 equals 3 * 91.0
274 equals 2 * 137.0
275 equals 5 * 55.0
276 equals 2 * 138.0
277 is a prime number
278 equals 2 * 139.0
279 equals 3 * 93.0
280 equals 2 * 140.0
281 is a prime number
282 equals 2 * 141.0
283 is a prime number
284 equals 2 * 142.0
285 equals 3 * 95.0
286 equals 2 * 143.0
287 equals 7 * 41.0
288 equals 2 * 144.0
289 equals 17 * 17.0
290 equals 2 * 145.0
291 equals 3 * 97.0
292 equals 2 * 146.0
293 is a prime number
294 equals 2 * 147.0
295 equals 5 * 59.0
296 equals 2 * 148.0
297 equals 3 * 99.0
298 equals 2 * 149.0
299 equals 13 * 23.0
300 equals 2 * 150.0
301 equals 7 * 43.0
302 equals 2 * 151.0
303 equals 3 * 101.0
304 equals 2 * 152.0
305 equals 5 * 61.0
306 equals 2 * 153.0
307 is a prime number
308 equals 2 * 154.0
309 equals 3 * 103.0
310 equals 2 * 155.0
311 is a prime number
312 equals 2 * 156.0
313 is a prime number
314 equals 2 * 157.0
315 equals 3 * 105.0
316 equals 2 * 158.0
317 is a prime number
318 equals 2 * 159.0
319 equals 11 * 29.0
320 equals 2 * 160.0
321 equals 3 * 107.0
322 equals 2 * 161.0
323 equals 17 * 19.0
324 equals 2 * 162.0
325 equals 5 * 65.0
326 equals 2 * 163.0
327 equals 3 * 109.0
328 equals 2 * 164.0
329 equals 7 * 47.0
330 equals 2 * 165.0
331 is a prime number
332 equals 2 * 166.0
333 equals 3 * 111.0
334 equals 2 * 167.0
335 equals 5 * 67.0
336 equals 2 * 168.0
337 is a prime number
338 equals 2 * 169.0
339 equals 3 * 113.0
340 equals 2 * 170.0
341 equals 11 * 31.0
342 equals 2 * 171.0
343 equals 7 * 49.0
344 equals 2 * 172.0
345 equals 3 * 115.0
346 equals 2 * 173.0
347 is a prime number
348 equals 2 * 174.0
349 is a prime number
350 equals 2 * 175.0
351 equals 3 * 117.0
352 equals 2 * 176.0
353 is a prime number
354 equals 2 * 177.0
355 equals 5 * 71.0
356 equals 2 * 178.0
357 equals 3 * 119.0
358 equals 2 * 179.0
359 is a prime number
360 equals 2 * 180.0
361 equals 19 * 19.0
362 equals 2 * 181.0
363 equals 3 * 121.0
364 equals 2 * 182.0
365 equals 5 * 73.0
366 equals 2 * 183.0
367 is a prime number
368 equals 2 * 184.0
369 equals 3 * 123.0
370 equals 2 * 185.0
371 equals 7 * 53.0
372 equals 2 * 186.0
373 is a prime number
374 equals 2 * 187.0
375 equals 3 * 125.0
376 equals 2 * 188.0
377 equals 13 * 29.0
378 equals 2 * 189.0
379 is a prime number
380 equals 2 * 190.0
381 equals 3 * 127.0
382 equals 2 * 191.0
383 is a prime number
384 equals 2 * 192.0
385 equals 5 * 77.0
386 equals 2 * 193.0
387 equals 3 * 129.0
388 equals 2 * 194.0
389 is a prime number
390 equals 2 * 195.0
391 equals 17 * 23.0
392 equals 2 * 196.0
393 equals 3 * 131.0
394 equals 2 * 197.0
395 equals 5 * 79.0
396 equals 2 * 198.0
397 is a prime number
398 equals 2 * 199.0
399 equals 3 * 133.0
400 equals 2 * 200.0
401 is a prime number
402 equals 2 * 201.0
403 equals 13 * 31.0
404 equals 2 * 202.0
405 equals 3 * 135.0
406 equals 2 * 203.0
407 equals 11 * 37.0
408 equals 2 * 204.0
409 is a prime number
410 equals 2 * 205.0
411 equals 3 * 137.0
412 equals 2 * 206.0
413 equals 7 * 59.0
414 equals 2 * 207.0
415 equals 5 * 83.0
416 equals 2 * 208.0
417 equals 3 * 139.0
418 equals 2 * 209.0
419 is a prime number
420 equals 2 * 210.0
421 is a prime number
422 equals 2 * 211.0
423 equals 3 * 141.0
424 equals 2 * 212.0
425 equals 5 * 85.0
426 equals 2 * 213.0
427 equals 7 * 61.0
428 equals 2 * 214.0
429 equals 3 * 143.0
430 equals 2 * 215.0
431 is a prime number
432 equals 2 * 216.0
433 is a prime number
434 equals 2 * 217.0
435 equals 3 * 145.0
436 equals 2 * 218.0
437 equals 19 * 23.0
438 equals 2 * 219.0
439 is a prime number
440 equals 2 * 220.0
441 equals 3 * 147.0
442 equals 2 * 221.0
443 is a prime number
444 equals 2 * 222.0
445 equals 5 * 89.0
446 equals 2 * 223.0
447 equals 3 * 149.0
448 equals 2 * 224.0
449 is a prime number
450 equals 2 * 225.0
451 equals 11 * 41.0
452 equals 2 * 226.0
453 equals 3 * 151.0
454 equals 2 * 227.0
455 equals 5 * 91.0
456 equals 2 * 228.0
457 is a prime number
458 equals 2 * 229.0
459 equals 3 * 153.0
460 equals 2 * 230.0
461 is a prime number
462 equals 2 * 231.0
463 is a prime number
464 equals 2 * 232.0
465 equals 3 * 155.0
466 equals 2 * 233.0
467 is a prime number
468 equals 2 * 234.0
469 equals 7 * 67.0
470 equals 2 * 235.0
471 equals 3 * 157.0
472 equals 2 * 236.0
473 equals 11 * 43.0
474 equals 2 * 237.0
475 equals 5 * 95.0
476 equals 2 * 238.0
477 equals 3 * 159.0
478 equals 2 * 239.0
479 is a prime number
480 equals 2 * 240.0
481 equals 13 * 37.0
482 equals 2 * 241.0
483 equals 3 * 161.0
484 equals 2 * 242.0
485 equals 5 * 97.0
486 equals 2 * 243.0
487 is a prime number
488 equals 2 * 244.0
489 equals 3 * 163.0
490 equals 2 * 245.0
491 is a prime number
492 equals 2 * 246.0
493 equals 17 * 29.0
494 equals 2 * 247.0
495 equals 3 * 165.0
496 equals 2 * 248.0
497 equals 7 * 71.0
498 equals 2 * 249.0
499 is a prime number
500 equals 2 * 250.0
501 equals 3 * 167.0
502 equals 2 * 251.0
503 is a prime number
504 equals 2 * 252.0
505 equals 5 * 101.0
506 equals 2 * 253.0
507 equals 3 * 169.0
508 equals 2 * 254.0
509 is a prime number
510 equals 2 * 255.0
511 equals 7 * 73.0
512 equals 2 * 256.0
513 equals 3 * 171.0
514 equals 2 * 257.0
515 equals 5 * 103.0
516 equals 2 * 258.0
517 equals 11 * 47.0
518 equals 2 * 259.0
519 equals 3 * 173.0
520 equals 2 * 260.0
521 is a prime number
522 equals 2 * 261.0
523 is a prime number
524 equals 2 * 262.0
525 equals 3 * 175.0
526 equals 2 * 263.0
527 equals 17 * 31.0
528 equals 2 * 264.0
529 equals 23 * 23.0
530 equals 2 * 265.0
531 equals 3 * 177.0
532 equals 2 * 266.0
533 equals 13 * 41.0
534 equals 2 * 267.0
535 equals 5 * 107.0
536 equals 2 * 268.0
537 equals 3 * 179.0
538 equals 2 * 269.0
539 equals 7 * 77.0
540 equals 2 * 270.0
541 is a prime number
542 equals 2 * 271.0
543 equals 3 * 181.0
544 equals 2 * 272.0
545 equals 5 * 109.0
546 equals 2 * 273.0
547 is a prime number
548 equals 2 * 274.0
549 equals 3 * 183.0
550 equals 2 * 275.0
551 equals 19 * 29.0
552 equals 2 * 276.0
553 equals 7 * 79.0
554 equals 2 * 277.0
555 equals 3 * 185.0
556 equals 2 * 278.0
557 is a prime number
558 equals 2 * 279.0
559 equals 13 * 43.0
560 equals 2 * 280.0
561 equals 3 * 187.0
562 equals 2 * 281.0
563 is a prime number
564 equals 2 * 282.0
565 equals 5 * 113.0
566 equals 2 * 283.0
567 equals 3 * 189.0
568 equals 2 * 284.0
569 is a prime number
570 equals 2 * 285.0
571 is a prime number
572 equals 2 * 286.0
573 equals 3 * 191.0
574 equals 2 * 287.0
575 equals 5 * 115.0
576 equals 2 * 288.0
577 is a prime number
578 equals 2 * 289.0
579 equals 3 * 193.0
580 equals 2 * 290.0
581 equals 7 * 83.0
582 equals 2 * 291.0
583 equals 11 * 53.0
584 equals 2 * 292.0
585 equals 3 * 195.0
586 equals 2 * 293.0
587 is a prime number
588 equals 2 * 294.0
589 equals 19 * 31.0
590 equals 2 * 295.0
591 equals 3 * 197.0
592 equals 2 * 296.0
593 is a prime number
594 equals 2 * 297.0
595 equals 5 * 119.0
596 equals 2 * 298.0
597 equals 3 * 199.0
598 equals 2 * 299.0
599 is a prime number
600 equals 2 * 300.0
601 is a prime number
602 equals 2 * 301.0
603 equals 3 * 201.0
604 equals 2 * 302.0
605 equals 5 * 121.0
606 equals 2 * 303.0
607 is a prime number
608 equals 2 * 304.0
609 equals 3 * 203.0
610 equals 2 * 305.0
611 equals 13 * 47.0
612 equals 2 * 306.0
613 is a prime number
614 equals 2 * 307.0
615 equals 3 * 205.0
616 equals 2 * 308.0
617 is a prime number
618 equals 2 * 309.0
619 is a prime number
620 equals 2 * 310.0
621 equals 3 * 207.0
622 equals 2 * 311.0
623 equals 7 * 89.0
624 equals 2 * 312.0
625 equals 5 * 125.0
626 equals 2 * 313.0
627 equals 3 * 209.0
628 equals 2 * 314.0
629 equals 17 * 37.0
630 equals 2 * 315.0
631 is a prime number
632 equals 2 * 316.0
633 equals 3 * 211.0
634 equals 2 * 317.0
635 equals 5 * 127.0
636 equals 2 * 318.0
637 equals 7 * 91.0
638 equals 2 * 319.0
639 equals 3 * 213.0
640 equals 2 * 320.0
641 is a prime number
642 equals 2 * 321.0
643 is a prime number
644 equals 2 * 322.0
645 equals 3 * 215.0
646 equals 2 * 323.0
647 is a prime number
648 equals 2 * 324.0
649 equals 11 * 59.0
650 equals 2 * 325.0
651 equals 3 * 217.0
652 equals 2 * 326.0
653 is a prime number
654 equals 2 * 327.0
655 equals 5 * 131.0
656 equals 2 * 328.0
657 equals 3 * 219.0
658 equals 2 * 329.0
659 is a prime number
660 equals 2 * 330.0
661 is a prime number
662 equals 2 * 331.0
663 equals 3 * 221.0
664 equals 2 * 332.0
665 equals 5 * 133.0
666 equals 2 * 333.0
667 equals 23 * 29.0
668 equals 2 * 334.0
669 equals 3 * 223.0
670 equals 2 * 335.0
671 equals 11 * 61.0
672 equals 2 * 336.0
673 is a prime number
674 equals 2 * 337.0
675 equals 3 * 225.0
676 equals 2 * 338.0
677 is a prime number
678 equals 2 * 339.0
679 equals 7 * 97.0
680 equals 2 * 340.0
681 equals 3 * 227.0
682 equals 2 * 341.0
683 is a prime number
684 equals 2 * 342.0
685 equals 5 * 137.0
686 equals 2 * 343.0
687 equals 3 * 229.0
688 equals 2 * 344.0
689 equals 13 * 53.0
690 equals 2 * 345.0
691 is a prime number
692 equals 2 * 346.0
693 equals 3 * 231.0
694 equals 2 * 347.0
695 equals 5 * 139.0
696 equals 2 * 348.0
697 equals 17 * 41.0
698 equals 2 * 349.0
699 equals 3 * 233.0
700 equals 2 * 350.0
701 is a prime number
702 equals 2 * 351.0
703 equals 19 * 37.0
704 equals 2 * 352.0
705 equals 3 * 235.0
706 equals 2 * 353.0
707 equals 7 * 101.0
708 equals 2 * 354.0
709 is a prime number
710 equals 2 * 355.0
711 equals 3 * 237.0
712 equals 2 * 356.0
713 equals 23 * 31.0
714 equals 2 * 357.0
715 equals 5 * 143.0
716 equals 2 * 358.0
717 equals 3 * 239.0
718 equals 2 * 359.0
719 is a prime number
720 equals 2 * 360.0
721 equals 7 * 103.0
722 equals 2 * 361.0
723 equals 3 * 241.0
724 equals 2 * 362.0
725 equals 5 * 145.0
726 equals 2 * 363.0
727 is a prime number
728 equals 2 * 364.0
729 equals 3 * 243.0
730 equals 2 * 365.0
731 equals 17 * 43.0
732 equals 2 * 366.0
733 is a prime number
734 equals 2 * 367.0
735 equals 3 * 245.0
736 equals 2 * 368.0
737 equals 11 * 67.0
738 equals 2 * 369.0
739 is a prime number
740 equals 2 * 370.0
741 equals 3 * 247.0
742 equals 2 * 371.0
743 is a prime number
744 equals 2 * 372.0
745 equals 5 * 149.0
746 equals 2 * 373.0
747 equals 3 * 249.0
748 equals 2 * 374.0
749 equals 7 * 107.0
750 equals 2 * 375.0
751 is a prime number
752 equals 2 * 376.0
753 equals 3 * 251.0
754 equals 2 * 377.0
755 equals 5 * 151.0
756 equals 2 * 378.0
757 is a prime number
758 equals 2 * 379.0
759 equals 3 * 253.0
760 equals 2 * 380.0
761 is a prime number
762 equals 2 * 381.0
763 equals 7 * 109.0
764 equals 2 * 382.0
765 equals 3 * 255.0
766 equals 2 * 383.0
767 equals 13 * 59.0
768 equals 2 * 384.0
769 is a prime number
770 equals 2 * 385.0
771 equals 3 * 257.0
772 equals 2 * 386.0
773 is a prime number
774 equals 2 * 387.0
775 equals 5 * 155.0
776 equals 2 * 388.0
777 equals 3 * 259.0
778 equals 2 * 389.0
779 equals 19 * 41.0
780 equals 2 * 390.0
781 equals 11 * 71.0
782 equals 2 * 391.0
783 equals 3 * 261.0
784 equals 2 * 392.0
785 equals 5 * 157.0
786 equals 2 * 393.0
787 is a prime number
788 equals 2 * 394.0
789 equals 3 * 263.0
790 equals 2 * 395.0
791 equals 7 * 113.0
792 equals 2 * 396.0
793 equals 13 * 61.0
794 equals 2 * 397.0
795 equals 3 * 265.0
796 equals 2 * 398.0
797 is a prime number
798 equals 2 * 399.0
799 equals 17 * 47.0
800 equals 2 * 400.0
801 equals 3 * 267.0
802 equals 2 * 401.0
803 equals 11 * 73.0
804 equals 2 * 402.0
805 equals 5 * 161.0
806 equals 2 * 403.0
807 equals 3 * 269.0
808 equals 2 * 404.0
809 is a prime number
810 equals 2 * 405.0
811 is a prime number
812 equals 2 * 406.0
813 equals 3 * 271.0
814 equals 2 * 407.0
815 equals 5 * 163.0
816 equals 2 * 408.0
817 equals 19 * 43.0
818 equals 2 * 409.0
819 equals 3 * 273.0
820 equals 2 * 410.0
821 is a prime number
822 equals 2 * 411.0
823 is a prime number
824 equals 2 * 412.0
825 equals 3 * 275.0
826 equals 2 * 413.0
827 is a prime number
828 equals 2 * 414.0
829 is a prime number
830 equals 2 * 415.0
831 equals 3 * 277.0
832 equals 2 * 416.0
833 equals 7 * 119.0
834 equals 2 * 417.0
835 equals 5 * 167.0
836 equals 2 * 418.0
837 equals 3 * 279.0
838 equals 2 * 419.0
839 is a prime number
840 equals 2 * 420.0
841 equals 29 * 29.0
842 equals 2 * 421.0
843 equals 3 * 281.0
844 equals 2 * 422.0
845 equals 5 * 169.0
846 equals 2 * 423.0
847 equals 7 * 121.0
848 equals 2 * 424.0
849 equals 3 * 283.0
850 equals 2 * 425.0
851 equals 23 * 37.0
852 equals 2 * 426.0
853 is a prime number
854 equals 2 * 427.0
855 equals 3 * 285.0
856 equals 2 * 428.0
857 is a prime number
858 equals 2 * 429.0
859 is a prime number
860 equals 2 * 430.0
861 equals 3 * 287.0
862 equals 2 * 431.0
863 is a prime number
864 equals 2 * 432.0
865 equals 5 * 173.0
866 equals 2 * 433.0
867 equals 3 * 289.0
868 equals 2 * 434.0
869 equals 11 * 79.0
870 equals 2 * 435.0
871 equals 13 * 67.0
872 equals 2 * 436.0
873 equals 3 * 291.0
874 equals 2 * 437.0
875 equals 5 * 175.0
876 equals 2 * 438.0
877 is a prime number
878 equals 2 * 439.0
879 equals 3 * 293.0
880 equals 2 * 440.0
881 is a prime number
882 equals 2 * 441.0
883 is a prime number
884 equals 2 * 442.0
885 equals 3 * 295.0
886 equals 2 * 443.0
887 is a prime number
888 equals 2 * 444.0
889 equals 7 * 127.0
890 equals 2 * 445.0
891 equals 3 * 297.0
892 equals 2 * 446.0
893 equals 19 * 47.0
894 equals 2 * 447.0
895 equals 5 * 179.0
896 equals 2 * 448.0
897 equals 3 * 299.0
898 equals 2 * 449.0
899 equals 29 * 31.0
900 equals 2 * 450.0
901 equals 17 * 53.0
902 equals 2 * 451.0
903 equals 3 * 301.0
904 equals 2 * 452.0
905 equals 5 * 181.0
906 equals 2 * 453.0
907 is a prime number
908 equals 2 * 454.0
909 equals 3 * 303.0
910 equals 2 * 455.0
911 is a prime number
912 equals 2 * 456.0
913 equals 11 * 83.0
914 equals 2 * 457.0
915 equals 3 * 305.0
916 equals 2 * 458.0
917 equals 7 * 131.0
918 equals 2 * 459.0
919 is a prime number
920 equals 2 * 460.0
921 equals 3 * 307.0
922 equals 2 * 461.0
923 equals 13 * 71.0
924 equals 2 * 462.0
925 equals 5 * 185.0
926 equals 2 * 463.0
927 equals 3 * 309.0
928 equals 2 * 464.0
929 is a prime number
930 equals 2 * 465.0
931 equals 7 * 133.0
932 equals 2 * 466.0
933 equals 3 * 311.0
934 equals 2 * 467.0
935 equals 5 * 187.0
936 equals 2 * 468.0
937 is a prime number
938 equals 2 * 469.0
939 equals 3 * 313.0
940 equals 2 * 470.0
941 is a prime number
942 equals 2 * 471.0
943 equals 23 * 41.0
944 equals 2 * 472.0
945 equals 3 * 315.0
946 equals 2 * 473.0
947 is a prime number
948 equals 2 * 474.0
949 equals 13 * 73.0
950 equals 2 * 475.0
951 equals 3 * 317.0
952 equals 2 * 476.0
953 is a prime number
954 equals 2 * 477.0
955 equals 5 * 191.0
956 equals 2 * 478.0
957 equals 3 * 319.0
958 equals 2 * 479.0
959 equals 7 * 137.0
960 equals 2 * 480.0
961 equals 31 * 31.0
962 equals 2 * 481.0
963 equals 3 * 321.0
964 equals 2 * 482.0
965 equals 5 * 193.0
966 equals 2 * 483.0
967 is a prime number
968 equals 2 * 484.0
969 equals 3 * 323.0
970 equals 2 * 485.0
971 is a prime number
972 equals 2 * 486.0
973 equals 7 * 139.0
974 equals 2 * 487.0
975 equals 3 * 325.0
976 equals 2 * 488.0
977 is a prime number
978 equals 2 * 489.0
979 equals 11 * 89.0
980 equals 2 * 490.0
981 equals 3 * 327.0
982 equals 2 * 491.0
983 is a prime number
984 equals 2 * 492.0
985 equals 5 * 197.0
986 equals 2 * 493.0
987 equals 3 * 329.0
988 equals 2 * 494.0
989 equals 23 * 43.0
990 equals 2 * 495.0
991 is a prime number
992 equals 2 * 496.0
993 equals 3 * 331.0
994 equals 2 * 497.0
995 equals 5 * 199.0
996 equals 2 * 498.0
997 is a prime number
998 equals 2 * 499.0
999 equals 3 * 333.0
>>> 
 RESTART: C:/Users/prosh/AppData/Local/Programs/Python/Python35-32/samples/primeNumber.py 
2 is a prime number
3 is a prime number
5 is a prime number
7 is a prime number
11 is a prime number
13 is a prime number
17 is a prime number
19 is a prime number
23 is a prime number
29 is a prime number
31 is a prime number
37 is a prime number
41 is a prime number
43 is a prime number
47 is a prime number
53 is a prime number
59 is a prime number
61 is a prime number
67 is a prime number
71 is a prime number
73 is a prime number
79 is a prime number
83 is a prime number
89 is a prime number
97 is a prime number
