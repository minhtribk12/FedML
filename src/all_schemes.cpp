/*
* Copyright (c) by the authors.
* This program is licensed under a
* Creative Commons Attribution-NonCommercial 3.0 Unported License.
* You should have received a copy of the license along with this
* work.  If not, see <http://creativecommons.org/licenses/by-nc/3.0/>.
* Authors: 
*/
void ::EncryptByJointPK(Ciphertext& cipher, Plaintext& plain,SecretKey& EncKey,Ciphertext& cipher1, Plaintext& plain1,SecretKey& EncKey1,Ciphertext& cipher2, Plaintext& plain2,SecretKey& EncKey2,Ciphertext& cipher3, Plaintext& plain3,SecretKey& EncKey3,Ciphertext& cipher4, Plaintext& plain4,SecretKey& EncKey4,Ciphertext& cipher5, Plaintext& plain5,SecretKey& EncKey5,Ciphertext& cipher6, Plaintext& plain6,SecretKey& EncKey6,Ciphertext& cipher7, Plaintext& plain7,SecretKey& EncKey7,Ciphertext& cipher8, Plaintext& plain8,SecretKey& EncKey8,Ciphertext& cipher9, Plaintext& plain9,SecretKey& EncKey9) {
	//TimeUtils timeutils;
	//Party0	
	Ring ring;
	cipher.logp = plain.logp;
	cipher.logq = plain.logq;
	cipher.n = plain.n;
	ZZ qQ = ring.qpows[plain.logq + logQ];
	ZZ* vx = new ZZ[N];
	ring.sampleZO(vx);	

	//timeutils.start("pk_generation");
	ZZ* axP = new ZZ[N];
	ZZ* bxP = new ZZ[N];
	long npP = ceil((1 + logQQ + logN + 2)/(double)pbnd);
	ring.sampleUniform2(axP, logQQ);
	ring.mult(bxP, EncKey.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP, QQ);
	Key* key = new Key();
	ring.CRT(key->rax, axP, nprimes);
	ring.CRT(key->rbx, bxP, nprimes);
	//timeutils.stop("pk_generation");
	

	
	//Party1
	cipher1.logp = plain1.logp;
	cipher1.logq = plain1.logq;
	cipher1.n = plain1.n;
	ZZ* bxP1 = new ZZ[N];
	ring.mult(bxP1, EncKey1.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP1, QQ);
	Key* key1 = new Key();
	ring.CRT(key1->rax, axP, nprimes);
	ring.CRT(key1->rbx, bxP1, nprimes);
	
	//Party2
	cipher2.logp = plain2.logp;
	cipher2.logq = plain2.logq;
	cipher2.n = plain2.n;
	ZZ* bxP2 = new ZZ[N];
	ring.mult(bxP2, EncKey2.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP2, QQ);
	Key* key2 = new Key();
	ring.CRT(key2->rax, axP, nprimes);
	ring.CRT(key2->rbx, bxP2, nprimes);

	//Party3
	cipher3.logp = plain3.logp;
	cipher3.logq = plain3.logq;
	cipher3.n = plain3.n;
	ZZ* bxP3 = new ZZ[N];
	ring.mult(bxP3, EncKey3.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP3, QQ);
	Key* key3 = new Key();
	ring.CRT(key3->rax, axP, nprimes);
	ring.CRT(key3->rbx, bxP3, nprimes);


	//Party4
	cipher4.logp = plain4.logp;
	cipher4.logq = plain4.logq;
	cipher4.n = plain4.n;
	ZZ* bxP4 = new ZZ[N];
	ring.mult(bxP4, EncKey4.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP4, QQ);
	Key* key4 = new Key();
	ring.CRT(key4->rax, axP, nprimes);
	ring.CRT(key4->rbx, bxP4, nprimes);


	//Party5
	cipher5.logp = plain5.logp;
	cipher5.logq = plain5.logq;
	cipher5.n = plain5.n;
	ZZ* bxP5 = new ZZ[N];
	ring.mult(bxP5, EncKey5.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP5, QQ);
	Key* key5 = new Key();
	ring.CRT(key5->rax, axP, nprimes);
	ring.CRT(key5->rbx, bxP5, nprimes);

	//Party6
	cipher6.logp = plain6.logp;
	cipher6.logq = plain6.logq;
	cipher6.n = plain6.n;
	ZZ* bxP6 = new ZZ[N];
	ring.mult(bxP6, EncKey6.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP6, QQ);
	Key* key6 = new Key();
	ring.CRT(key6->rax, axP, nprimes);
	ring.CRT(key6->rbx, bxP6, nprimes);


	//Party7
	cipher7.logp = plain7.logp;
	cipher7.logq = plain7.logq;
	cipher7.n = plain7.n;
	ZZ* bxP7 = new ZZ[N];
	ring.mult(bxP7, EncKey7.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP7, QQ);
	Key* key7 = new Key();
	ring.CRT(key7->rax, axP, nprimes);
	ring.CRT(key7->rbx, bxP7, nprimes);


	//Party8
	cipher8.logp = plain8.logp;
	cipher8.logq = plain8.logq;
	cipher8.n = plain8.n;
	ZZ* bxP8 = new ZZ[N];
	ring.mult(bxP8, EncKey8.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP8, QQ);
	Key* key8 = new Key();
	ring.CRT(key8->rax, axP, nprimes);
	ring.CRT(key8->rbx, bxP8, nprimes);


	//Party9
	cipher9.logp = plain9.logp;
	cipher9.logq = plain9.logq;
	cipher9.n = plain9.n;
	ZZ* bxP9 = new ZZ[N];
	ring.mult(bxP9, EncKey9.sx, axP, npP, QQ);
	ring.subFromGaussAndEqual(bxP9, QQ);
	Key* key9 = new Key();
	ring.CRT(key9->rax, axP, nprimes);
	ring.CRT(key9->rbx, bxP9, nprimes);

	//Sum of public joint keys

	//timeutils.start("joint_pk_generation");

	ZZ* bxSum = new ZZ[N];
	ring.addAndEqual(bxSum, bxP, QQ);
	ring.addAndEqual(bxSum, bxP1, QQ);
	ring.addAndEqual(bxSum, bxP2, QQ);
	ring.addAndEqual(bxSum, bxP3, QQ);
	ring.addAndEqual(bxSum, bxP4, QQ);
	ring.addAndEqual(bxSum, bxP5, QQ);
	ring.addAndEqual(bxSum, bxP6, QQ);
	ring.addAndEqual(bxSum, bxP7, QQ);
	ring.addAndEqual(bxSum, bxP8, QQ);
	ring.addAndEqual(bxSum, bxP9, QQ);
	
	Key* keySum = new Key();
	ring.CRT(keySum->rax, axP, nprimes);
	ring.CRT(keySum->rbx, bxSum, nprimes);
	//timeutils.stop("joint_pk_generation");
	delete[] axP; delete[] bxP;


	//Encrypt Party0
	//timeutils.start("encryption_one");
	ring.multNTT(cipher.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher.ax, qQ);
	ring.multNTT(cipher.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher.bx, qQ);
	ring.addAndEqual(cipher.bx, plain.mx, qQ);
	ring.rightShiftAndEqual(cipher.ax, logQ);
	ring.rightShiftAndEqual(cipher.bx, logQ);
	//timeutils.stop("encryption_one");

	//Encrypt Party1
	ring.multNTT(cipher1.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher1.ax, qQ);
	ring.multNTT(cipher1.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher1.bx, qQ);
	ring.addAndEqual(cipher1.bx, plain1.mx, qQ);
	ring.rightShiftAndEqual(cipher1.ax, logQ);
	ring.rightShiftAndEqual(cipher1.bx, logQ);
	//Encrypt Party2
	ring.multNTT(cipher2.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher2.ax, qQ);
	ring.multNTT(cipher2.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher2.bx, qQ);
	ring.addAndEqual(cipher2.bx, plain2.mx, qQ);
	ring.rightShiftAndEqual(cipher2.ax, logQ);
	ring.rightShiftAndEqual(cipher2.bx, logQ);

	//Encrypt Party3
	ring.multNTT(cipher3.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher3.ax, qQ);
	ring.multNTT(cipher3.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher3.bx, qQ);
	ring.addAndEqual(cipher3.bx, plain3.mx, qQ);
	ring.rightShiftAndEqual(cipher3.ax, logQ);
	ring.rightShiftAndEqual(cipher3.bx, logQ);

	//Encrypt Party4
	ring.multNTT(cipher4.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher4.ax, qQ);
	ring.multNTT(cipher4.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher4.bx, qQ);
	ring.addAndEqual(cipher4.bx, plain4.mx, qQ);
	ring.rightShiftAndEqual(cipher4.ax, logQ);
	ring.rightShiftAndEqual(cipher4.bx, logQ);


	//Encrypt Party5
	ring.multNTT(cipher5.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher5.ax, qQ);
	ring.multNTT(cipher5.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher5.bx, qQ);
	ring.addAndEqual(cipher5.bx, plain5.mx, qQ);
	ring.rightShiftAndEqual(cipher5.ax, logQ);
	ring.rightShiftAndEqual(cipher5.bx, logQ);




	//Encrypt Party6
	ring.multNTT(cipher6.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher6.ax, qQ);
	ring.multNTT(cipher6.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher6.bx, qQ);
	ring.addAndEqual(cipher6.bx, plain6.mx, qQ);
	ring.rightShiftAndEqual(cipher6.ax, logQ);
	ring.rightShiftAndEqual(cipher6.bx, logQ);

	//Encrypt Party7
	ring.multNTT(cipher7.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher7.ax, qQ);
	ring.multNTT(cipher7.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher7.bx, qQ);
	ring.addAndEqual(cipher7.bx, plain7.mx, qQ);
	ring.rightShiftAndEqual(cipher7.ax, logQ);
	ring.rightShiftAndEqual(cipher7.bx, logQ);


	//Encrypt Party8
	ring.multNTT(cipher8.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher8.ax, qQ);
	ring.multNTT(cipher8.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher8.bx, qQ);
	ring.addAndEqual(cipher8.bx, plain8.mx, qQ);
	ring.rightShiftAndEqual(cipher8.ax, logQ);
	ring.rightShiftAndEqual(cipher8.bx, logQ);

	//Encrypt Party9
	ring.multNTT(cipher9.ax, vx, keySum->rax, npP, qQ);
	ring.addGaussAndEqual(cipher9.ax, qQ);
	ring.multNTT(cipher9.bx, vx, keySum->rbx, npP, qQ);
	ring.addGaussAndEqual(cipher9.bx, qQ);
	ring.addAndEqual(cipher9.bx, plain9.mx, qQ);
	ring.rightShiftAndEqual(cipher9.ax, logQ);
	ring.rightShiftAndEqual(cipher9.bx, logQ);
	
	delete[] vx;
}




Key* ::Convert_to_key_structure(SecretKey& secretKey) {
	Ring ring;
	
	ZZ* ax = new ZZ[N];
	ZZ* bx = new ZZ[N];

	long np = ceil((1 + logQQ + logN + 2)/(double)pbnd);
	ring.sampleUniform2(ax, logQQ);
	ring.mult(bx, secretKey.sx, ax, np, QQ);
	ring.subFromGaussAndEqual(bx, QQ);

	Key* key = new Key();
	ring.CRT(key->rax, ax, nprimes);
	ring.CRT(key->rbx, bx, nprimes);
	delete[] ax; delete[] bx;	
	return key;
}


void ::xMK_CKKS_scheme(long logq, long logp, long logn) {

	int sum = 0;
	double x;
	ifstream inFile;
	long n= (1 << logn);
	ostringstream temp;
	temp << round;
	complex<double>* mvec = EvaluatorUtils::randomComplexArray(n);
	
	//Data import Party 0
	inFile.open(".../p0"+".txt");
	long i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec[i] = tmp;
	i++;
	}
	inFile.close();

	srand(time(NULL));
	SetNumThreads(8);
	





	
	//Data import Party 1
	complex<double>* mvec1 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p1"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec1[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();

	//Data import Party 2
	complex<double>* mvec2 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p2"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec2[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();

	//Data import Party 3
	complex<double>* mvec3 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p3"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec3[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 4
	complex<double>* mvec4 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p4"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec4[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 5
	complex<double>* mvec5 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p5"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec5[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 6
	complex<double>* mvec6 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p6"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec6[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 7
	complex<double>* mvec7 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p7"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec7[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 8
	complex<double>* mvec8 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p8"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec8[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	//Data import Party 9
	complex<double>* mvec9 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p9"+".txt");
	i=0;
	if (!inFile) {
	//cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec9[i] = tmp;
	i++;

	//cout << "Value = " << x << endl; 
	}

	inFile.close();


	


	//Part0 Preparation
	//timeutils.start("encoding_one_p");
	Ring ring;
	SecretKey secretKey(ring);
	Scheme scheme(secretKey, ring);
	Plaintext plain;
	scheme.encode(plain, mvec, n, logp, logq);
	Ciphertext cipher;
	//timeutils.stop("encoding_one_p");
	//Part1 Preparation
	Ring ring1;
	SecretKey secretKey1(ring1);
	Scheme scheme1(secretKey1, ring);
	Ciphertext cipher1;
	Plaintext plain1;
	scheme1.encode(plain1, mvec1, n, logp, logq);

	
	//Part2 Preparation
	Ring ring2;
	SecretKey secretKey2(ring2);
	Scheme scheme2(secretKey2, ring);
	Ciphertext cipher2;
	Plaintext plain2;
	scheme2.encode(plain2, mvec2, n, logp, logq);
	
	//Part3 Preparation
	Ring ring3;
	SecretKey secretKey3(ring3);
	Scheme scheme3(secretKey3, ring);
	Ciphertext cipher3;
	Plaintext plain3;
	scheme3.encode(plain3, mvec3, n, logp, logq);

	//Part4 Preparation
	Ring ring4;
	SecretKey secretKey4(ring4);
	Scheme scheme4(secretKey4, ring);
	Ciphertext cipher4;
	Plaintext plain4;
	scheme4.encode(plain4, mvec4, n, logp, logq);


	//Part5 Preparation
	Ring ring5;
	SecretKey secretKey5(ring5);
	Scheme scheme5(secretKey5, ring);
	Ciphertext cipher5;
	Plaintext plain5;
	scheme5.encode(plain5, mvec5, n, logp, logq);


	//Part6 Preparation
	Ring ring6;
	SecretKey secretKey6(ring6);
	Scheme scheme6(secretKey6, ring);
	Ciphertext cipher6;
	Plaintext plain6;
	scheme6.encode(plain6, mvec6, n, logp, logq);


	//Part7 Preparation
	Ring ring7;
	SecretKey secretKey7(ring7);
	Scheme scheme7(secretKey7, ring);
	Ciphertext cipher7;
	Plaintext plain7;
	scheme7.encode(plain7, mvec7, n, logp, logq);

	//Part8 Preparation
	Ring ring8;
	SecretKey secretKey8(ring8);
	Scheme scheme8(secretKey8, ring);
	Ciphertext cipher8;
	Plaintext plain8;
	scheme8.encode(plain8, mvec8, n, logp, logq);

	//Part9 Preparation
	Ring ring9;
	SecretKey secretKey9(ring9);
	Scheme scheme9(secretKey9, ring);
	Ciphertext cipher9;
	Plaintext plain9;
	scheme9.encode(plain9, mvec9, n, logp, logq);

	//Ecnryption
	EncryptByJointPK(cipher,plain,secretKey,cipher1,plain1,secretKey1,cipher2,plain2,secretKey2,cipher3,plain3,secretKey3,cipher4,plain4,secretKey4,cipher5,plain5,secretKey5,cipher6,plain6,secretKey6,cipher7,plain7,secretKey7,cipher8,plain8,secretKey8,cipher9,plain9,secretKey9);

	std::string contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
	cout<<"[LOG] : Transmission Data Size "<<contents.length()<<" Bytes.\n";
	//send files

	//timeutils.start("ciphers_sum");
	//Ciphers sum
void ::sumCiphers() {	
	Ring ring_1;
	Ciphertext cipherAdd;

	ZZ q1 = ring_1.qpows[cipher1.logq];
	ZZ q2 = ring_1.qpows[cipher2.logq];
	ZZ q3 = ring_1.qpows[cipher3.logq];
	ZZ q4 = ring_1.qpows[cipher4.logq];
	ZZ q5 = ring_1.qpows[cipher5.logq];
	ZZ q6 = ring_1.qpows[cipher6.logq];
	ZZ q7 = ring_1.qpows[cipher7.logq];
	ZZ q8 = ring_1.qpows[cipher8.logq];
	ZZ q9 = ring_1.qpows[cipher9.logq];

	cipherAdd.copyParams(cipher);
	
	ring.add(cipherAdd.ax, cipher.ax, cipher1.ax, q1);
	ring.add(cipherAdd.bx, cipher.bx, cipher1.bx, q1);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher2.ax, q2);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher2.bx, q2);
	
	ring.add(cipherAdd.ax, cipherAdd.ax, cipher3.ax, q3);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher3.bx, q3);
	
	ring.add(cipherAdd.ax, cipherAdd.ax, cipher4.ax, q4);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher4.bx, q4);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher5.ax, q5);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher5.bx, q5);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher6.ax, q6);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher6.bx, q6);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher7.ax, q7);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher7.bx, q7);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher8.ax, q8);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher8.bx, q8);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher9.ax, q9);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher9.bx, q9);
	//timeutils.stop("ciphers_sum");



	ZZ* sx = new ZZ[N];
	ZZ* sx1 = new ZZ[N];
	ZZ* sx3 = new ZZ[N];
	ZZ* sx4 = new ZZ[N];
	ZZ* sx5 = new ZZ[N];
	ZZ* sx6 = new ZZ[N];
	ZZ* sx7 = new ZZ[N];
	ZZ* sx8 = new ZZ[N];
	ZZ* sx9 = new ZZ[N];
	ZZ* sx10 = new ZZ[N];
	
	//New TEST
	Plaintext plain_t;
	Plaintext plain_t1;
	Plaintext plain_t2;
	Plaintext plain_t3;
	Plaintext plain_t4;
	Plaintext plain_t5;
	Plaintext plain_t6;
	Plaintext plain_t7;
	Plaintext plain_t8;
	Plaintext plain_t9;
	Plaintext plain_t10;

	ZZ q = ring.qpows[cipher.logq];
	plain_t.logp = cipher.logp;
	plain_t.logq = cipher.logq;
	plain_t.n = cipher.n;

	plain_t1.logp = cipher1.logp;
	plain_t1.logq = cipher1.logq;
	plain_t1.n = cipher1.n;


	plain_t2.logp = cipher2.logp;
	plain_t2.logq = cipher2.logq;
	plain_t2.n = cipher2.n;


	plain_t3.logp = cipher3.logp;
	plain_t3.logq = cipher3.logq;
	plain_t3.n = cipher3.n;

	plain_t4.logp = cipher4.logp;
	plain_t4.logq = cipher4.logq;
	plain_t4.n = cipher4.n;

	plain_t5.logp = cipher5.logp;
	plain_t5.logq = cipher5.logq;
	plain_t5.n = cipher5.n;

	plain_t6.logp = cipher6.logp;
	plain_t6.logq = cipher6.logq;
	plain_t6.n = cipher6.n;

	plain_t7.logp = cipher7.logp;
	plain_t7.logq = cipher7.logq;
	plain_t7.n = cipher7.n;

	plain_t8.logp = cipher8.logp;
	plain_t8.logq = cipher8.logq;
	plain_t8.n = cipher8.n;

	plain_t9.logp = cipher9.logp;
	plain_t9.logq = cipher9.logq;
	plain_t9.n = cipher9.n;
}
void ::DShare(long logq, long logp, long logn,string round) {


	//Decryption share p0
	//timeutils.start("dec_share_one_p");
	long np = ceil((1 + cipher1.logq + logN + 2)/(double)pbnd);
	ring.mult(plain_t.mx, cipherAdd.ax, secretKey.sx, np, q);
	//timeutils.stop("dec_share_one_p");
	ring.mult(plain_t1.mx, cipherAdd.ax, secretKey1.sx, np, q1);
	ring.mult(plain_t2.mx, cipherAdd.ax, secretKey2.sx, np, q2);
	ring.mult(plain_t3.mx, cipherAdd.ax, secretKey3.sx, np, q3);
	ring.mult(plain_t4.mx, cipherAdd.ax, secretKey4.sx, np, q4);
	ring.mult(plain_t5.mx, cipherAdd.ax, secretKey5.sx, np, q5);
	ring.mult(plain_t6.mx, cipherAdd.ax, secretKey6.sx, np, q6);
	ring.mult(plain_t7.mx, cipherAdd.ax, secretKey7.sx, np, q7);
	ring.mult(plain_t8.mx, cipherAdd.ax, secretKey8.sx, np, q8);
	ring.mult(plain_t9.mx, cipherAdd.ax, secretKey9.sx, np, q9);


}

void ::AddC0(long logq, long logp, long logn,string round) {
    ring.addAndEqual(plain_t.mx, plain_t1.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t2.mx, q);	
	ring.addAndEqual(plain_t.mx, plain_t3.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t4.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t5.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t6.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t7.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t8.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t9.mx, q);
	//Add C0 to Di sum
	//timeutils.start("add_C0");
	ring.addAndEqual(plain_t.mx, cipherAdd.bx, q);
	//timeutils.stop("add_C0");

	complex<double>* res=scheme.decode(plain_t);




}



	
	delete ring;
	scheme=new Scheme();
	plain_t=Plaintext();
	plain_t1=Plaintext();
	plain_t2=Plaintext();
	plain_t3=Plaintext();
	plain_t4=Plaintext();
	plain_t5=Plaintext();
	plain_t6=Plaintext();
	plain_t7=Plaintext();
	plain_t8=Plaintext();
	plain_t9=Plaintext();
	plain_t10=Plaintext();
	delete mvec;
	delete mvec1;
	delete mvec2;
	delete mvec3;
	delete mvec4;
	delete mvec5;	
	delete mvec6;
	delete mvec7;
	delete mvec8;
	delete mvec9;
	cipher.free();
	cipher1.free();
	cipher2.free();
	cipher3.free();
	cipher4.free();
	cipher5.free();
	cipher6.free();
	cipher7.free();	
	cipher8.free();
	cipher9.free();
	cipherAdd.free();
	delete resP;
	delete resP1;
	delete resP2;
	delete resP3;
	delete resP4;
	delete resP5;
	delete resP6;
	delete resP7;
	delete resP8;
	delete resP9;
	delete res;
	secretKey=new SecretKey();
	secretKey1=new SecretKey();
	secretKey2=new SecretKey();
	secretKey3=new SecretKey();
	secretKey4=new SecretKey();
	secretKey5=new SecretKey();
	secretKey6=new SecretKey();
	secretKey7=new SecretKey();
	secretKey8=new SecretKey();
	secretKey9=new SecretKey();
	
	return ;
	

}	


void ::MK_CKKS_scheme(long logq, long logp, long logn) {
	int sum = 0;
	double x;
	ifstream inFile;
	long n= (1 << logn);
	complex<double>* mvec = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p1.txt");
	long i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	
	while (inFile >> x) {

	

	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec[i] = tmp;
	i++;
	

	}

	inFile.close();



	cout << "!!! START TEST ENCRYPT !!!" << endl;
	srand(time(NULL));
	SetNumThreads(8);
	TimeUtils timeutils;
	Ring ring;
	SecretKey secretKey(ring);
	
	Scheme scheme(secretKey, ring);


	cout << "!!! Valus of n !!!" << endl;
	Plaintext plain;
	cout << n; 
	cout << "!!! Value of n !!!" << endl;
	
	Ciphertext cipher;

	timeutils.start("Encrypt");
	scheme.encrypt(cipher, mvec, n, logp, logq);

	Ring ring1;
	SecretKey secretKey1(ring1);
	
	
	Scheme scheme1(secretKey1, ring1);
	

	Plaintext plain1;


	complex<double>* mvec1 = EvaluatorUtils::randomComplexArray(n);

	inFile.open(".../p2.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	
	while (inFile >> x) {

	

	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec1[i] = tmp;
	i++;
	

	}

	inFile.close();

	Ciphertext cipher1;



	scheme1.encrypt(cipher1, mvec1, n, logp, logq);



	//Node=3
	complex<double>* mvec3 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p3.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec3[i] = tmp;
	i++;

	}
	inFile.close();


	Ring ring3;
	SecretKey secretKey3(ring3);
	Scheme scheme3(secretKey3, ring3);

	Ciphertext cipher3;
	scheme3.encrypt(cipher3, mvec3, n, logp, logq);


	//End node3
	
	//Node=4
	complex<double>* mvec4 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p4.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec4[i] = tmp;
	i++;
	cout << "Value = " << x << endl; 
	}
	inFile.close();
	Ring ring4;
	SecretKey secretKey4(ring4);
	Scheme scheme4(secretKey4, ring4);

	Ciphertext cipher4;


	//End node4

	//Node=5
	complex<double>* mvec5 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p5.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec5[i] = tmp;
	i++;
	cout << "Value = " << x << endl; 
	}
	inFile.close();


	Ring ring5;
	SecretKey secretKey5(ring5);
	Scheme scheme5(secretKey5, ring5);
	Ciphertext cipher5;
	scheme5.encrypt(cipher5, mvec5, n, logp, logq);

	//End node5


	//Node=6
	complex<double>* mvec6 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p6.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec6[i] = tmp;
	i++;

	}
	inFile.close();

	Ring ring6;
	SecretKey secretKey6(ring6);
	Scheme scheme6(secretKey6, ring6);

	Ciphertext cipher6;
	scheme6.encrypt(cipher6, mvec6, n, logp, logq);


	//End node6


	//Node=7
	complex<double>* mvec7 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p7txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec7[i] = tmp;
	i++;
	}
	inFile.close();
	Ring ring7;
	SecretKey secretKey7(ring7);
	Scheme scheme7(secretKey7, ring7);
	Ciphertext cipher7;
	scheme7.encrypt(cipher7, mvec7, n, logp, logq);


	//End node7



	//Node=8
	complex<double>* mvec8 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p8.txt");
	i=0;
	if (!inFile) {

	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec8[i] = tmp;
	i++;

	}
	inFile.close();

	Ring ring8;
	SecretKey secretKey8(ring8);
	Scheme scheme8(secretKey8, ring8);

	Ciphertext cipher8;
	scheme8.encrypt(cipher8, mvec8, n, logp, logq);


	//End node8



	//Node=9
	complex<double>* mvec9 = EvaluatorUtils::randomComplexArray(n);
	inFile.open(".../p9.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec9[i] = tmp;
	i++;

	}
	inFile.close();

	Ring ring9;
	SecretKey secretKey9(ring9);
	Scheme scheme9(secretKey9, ring9);

	Ciphertext cipher9;
	scheme9.encrypt(cipher9, mvec9, n, logp, logq);


	//End node9


	//Node=10
	complex<double>* mvec10 = EvaluatorUtils::randomComplexArray(n);
	inFile.open("..../p10.txt");
	i=0;
	if (!inFile) {
	cout << "Unable to open file";
	exit(1); // terminate with error
	}
	while (inFile >> x) {
	complex<double> tmp;
	tmp.real((double) x);
	tmp.imag((double) x);
	mvec10[i] = tmp;
	i++;

	}
	inFile.close();

	Ring ring10;
	SecretKey secretKey10(ring10);
	Scheme scheme10(secretKey10, ring10);

	Ciphertext cipher10;
	scheme10.encrypt(cipher10, mvec10, n, logp, logq);


	//End node10	
	std::string contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
	cout<<"[LOG] : Transmission Data Size "<<contents.length()<<" Bytes.\n";
	//send files

	//timeutils.start("ciphers_sum");
	//Ciphers sum
void ::sumCiphers() {	

	Ciphertext cipherAdd;
	ZZ q0 = ring.qpows[cipher.logq];
	cipherAdd.copyParams(cipher);
	ring.add(cipherAdd.ax, cipher.ax, cipher1.ax, q0);
	ring.add(cipherAdd.bx, cipher.bx, cipher1.bx, q0);
	
	ring.add(cipherAdd.ax, cipherAdd.ax, cipher3.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher3.bx, q0);
	
	ring.add(cipherAdd.ax, cipherAdd.ax, cipher4.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher4.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher5.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher5.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher6.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher6.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher7.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher7.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher8.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher8.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher9.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher9.bx, q0);

	ring.add(cipherAdd.ax, cipherAdd.ax, cipher10.ax, q0);
	ring.add(cipherAdd.bx, cipherAdd.bx, cipher10.bx, q0);
	//End of Node3
}

void ::DShare(long logq, long logp, long logn,string round) {
	ZZ* sx = new ZZ[N];
	ZZ* sx1 = new ZZ[N];
	ZZ* sx3 = new ZZ[N];
	ZZ* sx4 = new ZZ[N];
	ZZ* sx5 = new ZZ[N];
	ZZ* sx6 = new ZZ[N];
	ZZ* sx7 = new ZZ[N];
	ZZ* sx8 = new ZZ[N];
	ZZ* sx9 = new ZZ[N];
	ZZ* sx10 = new ZZ[N];
	
	//New TEST
	Plaintext plain_t;
	Plaintext plain_t1;
	Plaintext plain_t3;
	Plaintext plain_t4;
	Plaintext plain_t5;
	Plaintext plain_t6;
	Plaintext plain_t7;
	Plaintext plain_t8;
	Plaintext plain_t9;
	Plaintext plain_t10;

	ZZ q = ring.qpows[cipher1.logq];
	plain_t.logp = cipher1.logp;
	plain_t.logq = cipher1.logq;
	plain_t.n = cipher1.n;

	plain_t1.logp = cipher1.logp;
	plain_t1.logq = cipher1.logq;
	plain_t1.n = cipher1.n;

	plain_t3.logp = cipher3.logp;
	plain_t3.logq = cipher3.logq;
	plain_t3.n = cipher3.n;

	plain_t4.logp = cipher4.logp;
	plain_t4.logq = cipher4.logq;
	plain_t4.n = cipher4.n;

	plain_t5.logp = cipher5.logp;
	plain_t5.logq = cipher5.logq;
	plain_t5.n = cipher5.n;

	plain_t6.logp = cipher6.logp;
	plain_t6.logq = cipher6.logq;
	plain_t6.n = cipher6.n;

	plain_t7.logp = cipher7.logp;
	plain_t7.logq = cipher7.logq;
	plain_t7.n = cipher7.n;

	plain_t8.logp = cipher8.logp;
	plain_t8.logq = cipher8.logq;
	plain_t8.n = cipher8.n;

	plain_t9.logp = cipher9.logp;
	plain_t9.logq = cipher9.logq;
	plain_t9.n = cipher9.n;

	plain_t10.logp = cipher10.logp;
	plain_t10.logq = cipher10.logq;
	plain_t10.n = cipher10.n;


	long np = ceil((1 + cipher1.logq + logN + 2)/(double)pbnd);
	ring.mult(plain_t.mx, cipher.ax, secretKey.sx, np, q);
	ring.mult(plain_t1.mx, cipher1.ax, secretKey1.sx, np, q);
	ring.mult(plain_t3.mx, cipher3.ax, secretKey3.sx, np, q);
	ring.mult(plain_t4.mx, cipher4.ax, secretKey4.sx, np, q);
	ring.mult(plain_t5.mx, cipher5.ax, secretKey5.sx, np, q);
	ring.mult(plain_t6.mx, cipher6.ax, secretKey6.sx, np, q);
	ring.mult(plain_t7.mx, cipher7.ax, secretKey7.sx, np, q);
	ring.mult(plain_t8.mx, cipher8.ax, secretKey8.sx, np, q);
	ring.mult(plain_t9.mx, cipher9.ax, secretKey9.sx, np, q);
	ring.mult(plain_t10.mx, cipher10.ax, secretKey10.sx, np, q);

}

void ::AddC0(long logq, long logp, long logn,string round) {
    ring.addAndEqual(plain_t.mx, plain_t1.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t3.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t4.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t5.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t6.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t7.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t8.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t9.mx, q);
	ring.addAndEqual(plain_t.mx, plain_t10.mx, q);	

    //Add C0 to the sum
	ring.addAndEqual(plain_t.mx, cipherAdd.bx, q);
	complex<double>* res=scheme1.decode(plain_t);
}
	
    delete ring;
	scheme=new Scheme();
	plain_t=Plaintext();
	plain_t1=Plaintext();
	plain_t2=Plaintext();
	plain_t3=Plaintext();
	plain_t4=Plaintext();
	plain_t5=Plaintext();
	plain_t6=Plaintext();
	plain_t7=Plaintext();
	plain_t8=Plaintext();
	plain_t9=Plaintext();
	plain_t10=Plaintext();
	delete mvec;
	delete mvec1;
	delete mvec2;
	delete mvec3;
	delete mvec4;
	delete mvec5;	
	delete mvec6;
	delete mvec7;
	delete mvec8;
	delete mvec9;
	cipher.free();
	cipher1.free();
	cipher2.free();
	cipher3.free();
	cipher4.free();
	cipher5.free();
	cipher6.free();
	cipher7.free();	
	cipher8.free();
	cipher9.free();
	cipherAdd.free();
	delete resP;
	delete resP1;
	delete resP2;
	delete resP3;
	delete resP4;
	delete resP5;
	delete resP6;
	delete resP7;
	delete resP8;
	delete resP9;
	delete res;
	secretKey=new SecretKey();
	secretKey1=new SecretKey();
	secretKey2=new SecretKey();
	secretKey3=new SecretKey();
	secretKey4=new SecretKey();
	secretKey5=new SecretKey();
	secretKey6=new SecretKey();
	secretKey7=new SecretKey();
	secretKey8=new SecretKey();
	secretKey9=new SecretKey();
	
	return ;
	
}	


void ::Main(long logq, long logp, long logn) {

call xMK_CKKS_scheme(~)
call MK_CKKS_scheme(~)
}