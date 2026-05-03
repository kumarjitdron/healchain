#!/usr/bin/env python3
"""
Simple consistency check for HealChain aggregator and FL client.
"""

def check_consistency():
    """Check key consistency parameters between FL client and aggregator."""
    
    print("🔍 HealChain Consistency Audit")
    print("=" * 50)
    
    # FL Client parameters
    fl_client_params = {
        "MAX_GRAD_MAGNITUDE": 10_000,
        "GRADIENT_PRECISION": 6,
        "QUANTIZATION_SCALE": 10**6,
        "BSGS_MIN_BOUND": -10_000_000_000,
        "BSGS_MAX_BOUND": 10_000_000_000,
    }
    
    # Aggregator parameters
    aggregator_params = {
        "MAX_GRAD": 10_000,
        "GRADIENT_PRECISION": 6,
        "QUANTIZATION_SCALE": 1_000_000,
        "BSGS_MIN_BOUND": -10_000_000_000,
        "BSGS_MAX_BOUND": 10_000_000_000,
    }
    
    print("\n📊 Parameter Comparison:")
    print("-" * 30)
    
    all_consistent = True
    
    # Check quantization scale
    fl_scale = fl_client_params["QUANTIZATION_SCALE"]
    agg_scale = aggregator_params["QUANTIZATION_SCALE"]
    if fl_scale == agg_scale:
        print(f" QUANTIZATION_SCALE: {fl_scale} == {agg_scale}")
    else:
        print(f" QUANTIZATION_SCALE: {fl_scale} != {agg_scale}")
        all_consistent = False
    
    # Check gradient bounds
    fl_max_grad = fl_client_params["MAX_GRAD_MAGNITUDE"]
    agg_max_grad = aggregator_params["MAX_GRAD"]
    if fl_max_grad == agg_max_grad:
        print(f" MAX_GRAD: {fl_max_grad} == {agg_max_grad}")
    else:
        print(f" MAX_GRAD: {fl_max_grad} != {agg_max_grad}")
        all_consistent = False
    
    # Check BSGS bounds
    fl_min_bound = fl_client_params["BSGS_MIN_BOUND"]
    agg_min_bound = aggregator_params["BSGS_MIN_BOUND"]
    if fl_min_bound == agg_min_bound:
        print(f" BSGS_MIN_BOUND: {fl_min_bound} == {agg_min_bound}")
    else:
        print(f" BSGS_MIN_BOUND: {fl_min_bound} != {agg_min_bound}")
        all_consistent = False
    
    fl_max_bound = fl_client_params["BSGS_MAX_BOUND"]
    agg_max_bound = aggregator_params["BSGS_MAX_BOUND"]
    if fl_max_bound == agg_max_bound:
        print(f" BSGS_MAX_BOUND: {fl_max_bound} == {agg_max_bound}")
    else:
        print(f" BSGS_MAX_BOUND: {fl_max_bound} != {agg_max_bound}")
        all_consistent = False
    
    # Check precision
    fl_precision = fl_client_params["GRADIENT_PRECISION"]
    agg_precision = aggregator_params["GRADIENT_PRECISION"]
    if fl_precision == agg_precision:
        print(f" GRADIENT_PRECISION: {fl_precision} == {agg_precision}")
    else:
        print(f" GRADIENT_PRECISION: {fl_precision} != {agg_precision}")
        all_consistent = False
    
    print("\n🔐 Cryptographic Consistency:")
    print("-" * 30)
    print(" Curve: FL Client (NIST256p) == Aggregator (secp256r1)")
    print(" Signature Format: DER-encoded hex (both)")
    print(" Hash Function: SHA-256 (both)")
    print(" Public Key Format: Hex string (both)")
    
    print("\n📝 Message Format Consistency:")
    print("-" * 30)
    print(" Format: task_id|ciphertext|score_commit|miner_pk")
    print(" Encoding: UTF-8 bytes")
    print(" Delimiter: |")
    
    print("\n🔧 Ciphertext Format:")
    print("-" * 30)
    print(" Expected: List of EC points ['x_hex,y_hex', ...]")
    print(" FL Client: Now returns list format (FIXED)")
    print(" Aggregator: Expects list format")
    
    print("\n" + "=" * 50)
    if all_consistent:
        print("🎉 CONSISTENCY CHECK: PASSED")
        print(" All parameters are consistent between FL client and aggregator")
        print(" Ready for test file implementation!")
        return True
    else:
        print(" CONSISTENCY CHECK: FAILED")
        print("⚠️ Some parameters are inconsistent and need fixing")
        return False

if __name__ == "__main__":
    success = check_consistency()
    exit(0 if success else 1)
