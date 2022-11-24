fn main() {
    for n in 0..10 {
      println!("{n}: Hello, Rust!");
    }

    let a = 10;
    let aref1 = &a;
    let aref2 = &a;
    println!("{}, {}, {}", a, aref1, aref2);

    let mut a = 10;
    let a_ref1 = &a;
    let a_mut_ref1 = &mut a;
    let a_mut_ref2 = &mut a;
    //*a_mut_ref1 = 20; // error.
    *a_mut_ref2 = 20;
    println!("{}", a);
    //println!("{}", a_ref1); // error.

    let a = 42;
    let ref_ref_ref_a = &&&a;
    let ref_a = **ref_ref_ref_a;
    let b = *ref_a;
    println!("{} {}", a, b);
    //println!("{}", a == ref_a); // error.

    let (x,y,z) = (1,2,3);
    let (a,b,c) = (4,5,6);
    let (i,_,_) = (7,8,9);
    println!("xyz= {} {} {}", x, y, z);
    println!("abc= {} {} {}", a, b, c);
    println!("  i= {}", i);

}
